import customtkinter as ctk
import qrcode
from PIL import Image
from tkinter import filedialog, messagebox

# Hyper-3D Neo-brutalist palette
BG_CANVAS = "#FFFDF9"        # Cream / off-white background
CARD_BG = "#FFFFFF"          # Pure white container surfaces
BORDER_COLOR = "#000000"     # Heavy solid black
ACCENT_YELLOW = "#FFD000"    # High-intensity, vibrant yellow-gold
ACCENT_GREEN = "#1AEB6B"     # Saturated, punchy action green
TEXT_COLOR = "#000000"       # High-contrast black text


class BrutalistQRApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("QR Code Genr.")
        self.geometry("480x720")
        self.resizable(False, False)
        self.configure(fg_color=BG_CANVAS)

        self.current_qr_img = None

        self._build_ui()

    def _build_ui(self):
        # Top-level window margins & shadow offset wrapper
        main_container = ctk.CTkFrame(self, fg_color="transparent")
        main_container.pack(fill="both", expand=True, padx=24, pady=24)

        # 1. Brutalist Title Header with 3D Offset Shadow effect
        title_shadow = ctk.CTkFrame(
            main_container,
            fg_color=BORDER_COLOR,
            corner_radius=0,
            height=68,
        )
        title_shadow.pack(fill="x", pady=(0, 16))
        title_shadow.pack_propagate(False)

        # Foreground plate offset to create "extrusion" shadow
        title_box = ctk.CTkFrame(
            title_shadow,
            fg_color=ACCENT_YELLOW,
            border_color=BORDER_COLOR,
            border_width=3,
            corner_radius=0,
        )
        title_box.place(relx=0, rely=0, relwidth=0.98, relheight=0.92)

        title_label = ctk.CTkLabel(
            title_box,
            text="⚡ 𝚀𝚁 𝙲𝙾𝙳𝙴 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙾𝚁",
            font=ctk.CTkFont(family="Arial Black", size=20, weight="bold"),
            text_color=TEXT_COLOR,
        )
        title_label.pack(pady=10)

        # 2. Input Container Card with offset 3D shadow backer
        card_shadow = ctk.CTkFrame(
            main_container,
            fg_color=BORDER_COLOR,
            corner_radius=0,
            height=160,
        )
        card_shadow.pack(fill="x", pady=8)
        card_shadow.pack_propagate(False)

        input_card = ctk.CTkFrame(
            card_shadow,
            fg_color=CARD_BG,
            border_color=BORDER_COLOR,
            border_width=3,
            corner_radius=0,
        )
        input_card.place(relx=0, rely=0, relwidth=0.98, relheight=0.96)

        input_tag = ctk.CTkLabel(
            input_card,
            text="[ INPUT LINK / TEXT ]",
            font=ctk.CTkFont(family="Courier New", size=13, weight="bold"),
            text_color=TEXT_COLOR,
        )
        input_tag.pack(anchor="w", padx=14, pady=(8, 2))

        self.entry = ctk.CTkEntry(
            input_card,
            placeholder_text="HTTPS://...",
            font=ctk.CTkFont(family="Consolas", size=13),
            fg_color="#F4F4F4",
            text_color=TEXT_COLOR,
            placeholder_text_color="#555555",
            border_color=BORDER_COLOR,
            border_width=2,
            corner_radius=0,
            height=36,
        )
        self.entry.pack(fill="x", padx=14, pady=(0, 10))
        self.entry.bind("<Return>", lambda e: self.generate_qr())

        # Massive High-Contrast, Vibrant 3D Generate Button
        gen_shadow = ctk.CTkFrame(
            input_card,
            fg_color=BORDER_COLOR,
            corner_radius=0,
            height=46,
        )
        gen_shadow.pack(fill="x", padx=14, pady=(0, 12))
        gen_shadow.pack_propagate(False)

        self.gen_btn = ctk.CTkButton(
            gen_shadow,
            text="GENERATE QR CODE ➔",
            font=ctk.CTkFont(family="Arial Black", size=14, weight="bold"),
            fg_color=ACCENT_YELLOW,
            hover_color="#E5AA00",  # Saturated golden click state
            text_color=TEXT_COLOR,
            border_color=BORDER_COLOR,
            border_width=3,
            corner_radius=0,
            height=40,
            command=self.generate_qr,
        )
        self.gen_btn.place(relx=0, rely=0, relwidth=0.97, relheight=0.88)

        # 3. QR Code Display Canvas Frame (Double Bevel)
        display_shadow = ctk.CTkFrame(
            main_container,
            width=270,
            height=270,
            fg_color=BORDER_COLOR,
            corner_radius=0,
        )
        display_shadow.pack(pady=12)
        display_shadow.pack_propagate(False)

        self.display_frame = ctk.CTkFrame(
            display_shadow,
            fg_color=CARD_BG,
            border_color=BORDER_COLOR,
            border_width=3,
            corner_radius=0,
        )
        self.display_frame.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)

        self.preview_label = ctk.CTkLabel(
            self.display_frame,
            text="[ NO QR DATA ]\nENTER URL ABOVE",
            font=ctk.CTkFont(family="Courier New", size=12, weight="bold"),
            text_color="#D4CFCC",
        )
        self.preview_label.pack(expand=True)

        # 4. Save Button with bottom offset Shadow (Green Accent)
        save_shadow = ctk.CTkFrame(
            main_container,
            fg_color=BORDER_COLOR,
            corner_radius=0,
            height=52,
        )
        save_shadow.pack(fill="x", pady=(10, 0))
        save_shadow.pack_propagate(False)

        self.save_btn = ctk.CTkButton(
            save_shadow,
            text="SAVE IMAGE TO DISK",
            font=ctk.CTkFont(family="Arial Black", size=14, weight="bold"),
            fg_color=ACCENT_GREEN,
            hover_color="#17C359",
            text_color=TEXT_COLOR,
            border_color=BORDER_COLOR,
            border_width=3,
            corner_radius=0,
            height=46,
            state="disabled",
            command=self.save_qr,
        )
        self.save_btn.place(relx=0, rely=0, relwidth=0.98, relheight=0.90)

    def generate_qr(self):
        data = self.entry.get().strip()
        if not data:
            messagebox.showwarning("ERR: EMPTY", "INPUT FIELD CANNOT BE EMPTY.")
            return

        # Build QR matrix
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=2,
        )
        qr.add_data(data)
        qr.make(fit=True)

        pil_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        self.current_qr_img = pil_img

        preview_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(240, 240))
        self.preview_label.configure(image=preview_img, text="")
        self.qr_label_reference = preview_img  # Prevent garbage collection

        self.save_btn.configure(state="normal")

    def save_qr(self):
        if not self.current_qr_img:
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")],
            title="EXPORT QR CODE",
        )
        if file_path:
            self.current_qr_img.save(file_path)
            messagebox.showinfo("SUCCESS", f"SAVED TO:\n{file_path}")


if __name__ == "__main__":
    app = BrutalistQRApp()
    app.mainloop()
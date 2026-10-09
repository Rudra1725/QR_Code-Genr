import io
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import qrcode
from PIL import Image

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class QRCodeApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("QR Code Studio")
        self.geometry("460x620")
        self.resizable(False, False)

        self.current_qr_img = None

        self._build_ui()

    def _build_ui(self):
        self.title_label = ctk.CTkLabel(
            self,
            text="QR Code Generator",
            font=ctk.CTkFont(size=22, weight="bold"),
        )
        self.title_label.pack(pady=(24, 6))

        self.subtitle_label = ctk.CTkLabel(
            self,
            text="Paste any URL or text below to generate your QR code",
            font=ctk.CTkFont(size=13),
            text_color="gray70",
        )
        self.subtitle_label.pack(pady=(0, 20))

        self.input_frame = ctk.CTkFrame(self, corner_radius=12)
        self.input_frame.pack(fill="x", padx=28, pady=(0, 16))

        self.url_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="https://example.com or plain text...",
            height=42,
            font=ctk.CTkFont(size=13),
        )
        self.url_entry.pack(fill="x", padx=14, pady=(14, 10))
        self.url_entry.bind("<Return>", lambda event: self.generate_qr())

        self.generate_btn = ctk.CTkButton(
            self.input_frame,
            text="Generate QR Code",
            height=38,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.generate_qr,
        )
        self.generate_btn.pack(fill="x", padx=14, pady=(0, 14))

        self.preview_frame = ctk.CTkFrame(
            self, width=270, height=270, corner_radius=12
        )
        self.preview_frame.pack(pady=10)
        self.preview_frame.pack_propagate(False)

        self.qr_label = ctk.CTkLabel(
            self.preview_frame,
            text="Your QR code preview\nwill appear here",
            font=ctk.CTkFont(size=13),
            text_color="gray60",
        )
        self.qr_label.pack(expand=True)

        self.save_btn = ctk.CTkButton(
            self,
            text="Save to Disk",
            height=38,
            state="disabled",
            fg_color="#2E7D32",
            hover_color="#1B5E20",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.save_qr,
        )
        self.save_btn.pack(fill="x", padx=28, pady=(16, 20))

    def generate_qr(self):
        data = self.url_entry.get().strip()

        if not data:
            messagebox.showwarning("Input Missing", "Please enter a valid link or text.")
            return

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
        self.qr_label.configure(image=preview_img, text="")
        self.qr_label.image = preview_img

    
        self.save_btn.configure(state="normal")

    def save_qr(self):
        if not self.current_qr_img:
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("All Files", "*.*")],
            title="Save QR Code",
        )

        if file_path:
            self.current_qr_img.save(file_path)
            messagebox.showinfo("Success", f"Saved successfully to:\n{file_path}")


if __name__ == "__main__":
    app = QRCodeApp()
    app.mainloop()
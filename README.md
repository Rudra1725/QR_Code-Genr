<div align="center">

# ⚡ QR Code Studio

**A sleek, modern desktop QR code generator built with Python and CustomTkinter.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-CustomTkinter-3B8ED0)](https://github.com/TomSchimansky/CustomTkinter)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](#)

</div>

---

## 📌 Overview

**QR Code Studio** (`QR_Code-Genr`) is a lightweight desktop utility designed to generate clean, high-contrast QR codes directly from links, text, or data. Styled with **CustomTkinter** for a native dark-mode experience, it generates live previews instantly and exports production-ready image files.

---

## ✨ Features

- **Modern Dark UI:** Clean rounded interface built with `customtkinter`.
- **Instant Live Preview:** Dynamic rendering directly inside the app window.
- **High-Correction Factor:** Uses `ERROR_CORRECT_H` (~30% error correction) so QR codes remain readable even when printed small or damaged.
- **One-Click Export:** Save generated codes as `.png`, `.jpg`, or `.jpeg` via native file dialogs.
- **Keyboard Shortcut:** Hit `Enter` in the input field to generate instantly without clicking.

---

## 📸 Preview

```text
+------------------------------------------+
|            QR Code Studio                |
|  Paste any URL or text below...          |
|                                          |
|  [ [https://example.com](https://example.com)                 ] |
|  [         Generate QR Code            ] |
|                                          |
|       +--------------------------+       |
|       |                          |       |
|       |      [ QR PREVIEW ]      |       |
|       |                          |       |
|       +--------------------------+       |
|                                          |
|  [           Save to Disk              ] |
+------------------------------------------+

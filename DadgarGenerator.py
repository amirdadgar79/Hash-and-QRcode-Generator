import hashlib
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import qrcode

def generate_qr():
    text = text_entry.get()
    algorithm = algorithm_var.get()
    save_location = save_location_entry.get()
    image_name = image_name_entry.get()

    if algorithm == "MD5":
        hashed_text = hashlib.md5(text.encode()).hexdigest()
    elif algorithm == "SHA256":
        hashed_text = hashlib.sha256(text.encode()).hexdigest()
    elif algorithm == "bcrypt":
        
        import bcrypt
        hashed_text = bcrypt.hashpw(text.encode(), bcrypt.gensalt()).decode()
    else:
        hashed_text = ""

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(hashed_text)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")
    save_path = f"{save_location}/{image_name}.png"
    qr_image.save(save_path)
    qr_image.show()


window = tk.Tk()
window.title("Hash and QR Code Generator")
window.geometry("500x400")


text_label = ttk.Label(window, text="Enter Text:")
text_label.pack()

text_entry = ttk.Entry(window)
text_entry.pack()


algorithm_var = tk.StringVar()
algorithm_label = ttk.Label(window, text="Select Algorithm:")
algorithm_label.pack()

algorithm_dropdown = ttk.Combobox(window, textvariable=algorithm_var, values=["MD5", "SHA256", "bcrypt"])
algorithm_dropdown.pack()


algorithm_dropdown.current(0)


save_location_label = ttk.Label(window, text="Save Location:")
save_location_label.pack()

save_location_entry = ttk.Entry(window)
save_location_entry.pack()


def browse_save_location():
    save_location = filedialog.askdirectory()
    save_location_entry.delete(0, tk.END)
    save_location_entry.insert(0, save_location)

browse_button = ttk.Button(window, text="Browse", command=browse_save_location)
browse_button.pack()


image_name_label = ttk.Label(window, text="Image Name:")
image_name_label.pack()

image_name_entry = ttk.Entry(window)
image_name_entry.pack()


generate_button = ttk.Button(window, text="Generate QR Code", command=generate_qr)
generate_button.pack()


window.mainloop()

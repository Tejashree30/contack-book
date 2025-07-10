import tkinter as tk
from tkinter import messagebox, simpledialog

# Main contact dictionary: key = name, value = dictionary of details
contacts = {}

# Add Contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required fields!")
        return

    if name in contacts:
        messagebox.showwarning("Warning", "Contact already exists!")
    else:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        messagebox.showinfo("Success", f"Contact '{name}' added.")
        clear_entries()
        refresh_listbox()

# View Contacts
def refresh_listbox():
    contact_listbox.delete(0, tk.END)
    for name in contacts:
        contact_listbox.insert(tk.END, f"{name} - {contacts[name]['Phone']}")

# Search Contact
def search_contact():
    search_term = search_entry.get().strip().lower()
    contact_listbox.delete(0, tk.END)
    for name, details in contacts.items():
        if search_term in name.lower() or search_term in details['Phone']:
            contact_listbox.insert(tk.END, f"{name} - {details['Phone']}")

# Display selected contact details
def show_selected_contact(event):
    selected = contact_listbox.curselection()
    if selected:
        name = contact_listbox.get(selected[0]).split(" - ")[0]
        details = contacts.get(name)
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        name_entry.insert(0, name)
        phone_entry.insert(0, details['Phone'])
        email_entry.insert(0, details['Email'])
        address_entry.insert(0, details['Address'])

# Update Contact
def update_contact():
    name = name_entry.get().strip()
    if name in contacts:
        contacts[name]['Phone'] = phone_entry.get().strip()
        contacts[name]['Email'] = email_entry.get().strip()
        contacts[name]['Address'] = address_entry.get().strip()
        messagebox.showinfo("Success", f"Contact '{name}' updated.")
        refresh_listbox()
    else:
        messagebox.showerror("Error", "Contact does not exist.")

# Delete Contact
def delete_contact():
    name = name_entry.get().strip()
    if name in contacts:
        if messagebox.askyesno("Confirm", f"Delete contact '{name}'?"):
            del contacts[name]
            messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")
            clear_entries()
            refresh_listbox()
    else:
        messagebox.showerror("Error", "Contact not found.")

# Clear all entries
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Contact Manager")
root.geometry("700x500")
root.config(bg="#f8f8f8")

# === Title ===
title_label = tk.Label(root, text="Contact Manager App", font=("Arial", 20, "bold"), bg="#f8f8f8", fg="#333")
title_label.pack(pady=10)

# === Input Frame ===
input_frame = tk.Frame(root, bg="#f8f8f8")
input_frame.pack(pady=5)

# Name
tk.Label(input_frame, text="Name:", font=("Arial", 12), bg="#f8f8f8").grid(row=0, column=0, sticky='e')
name_entry = tk.Entry(input_frame, font=("Arial"W, 12), width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Phone
tk.Label(input_frame, text="Phone:", font=("Arial", 12), bg="#f8f8f8").grid(row=1, column=0, sticky='e')
phone_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

# Email
tk.Label(input_frame, text="Email:", font=("Arial", 12), bg="#f8f8f8").grid(row=2, column=0, sticky='e')
email_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
email_entry.grid(row=2, column=1, padx=10, pady=5)

# Address
tk.Label(input_frame, text="Address:", font=("Arial", 12), bg="#f8f8f8").grid(row=3, column=0, sticky='e')
address_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# === Button Frame ===
button_frame = tk.Frame(root, bg="#f8f8f8")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", font=("Arial", 12), width=10, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Update", font=("Arial", 12), width=10, command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete", font=("Arial", 12), width=10, command=delete_contact).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Clear", font=("Arial", 12), width=10, command=clear_entries).grid(row=0, column=3, padx=5)

# === Search and Contact List ===
search_frame = tk.Frame(root, bg="#f8f8f8")
search_frame.pack(pady=10)

search_entry = tk.Entry(search_frame, font=("Arial", 12), width=30)
search_entry.grid(row=0, column=0, padx=10)

tk.Button(search_frame, text="Search", font=("Arial", 12), command=search_contact).grid(row=0, column=1, padx=5)
tk.Button(search_frame, text="Show All", font=("Arial", 12), command=refresh_listbox).grid(row=0, column=2, padx=5)

# Contact list
contact_listbox = tk.Listbox(root, font=("Arial", 12), width=60, height=10)
contact_listbox.pack(pady=10)
contact_listbox.bind("<<ListboxSelect>>", show_selected_contact)

# Start
refresh_listbox()
root.mainloop()

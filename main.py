from account_menu import Menu
import tkinter as tk

def main():
    root = tk.Tk()
    app = Menu(root)  # Start the dashboard/menu
    root.mainloop()

if __name__ == "__main__":
    main()

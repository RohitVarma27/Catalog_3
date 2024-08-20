import tkinter as tk
from tkinter import messagebox


class Auction:
    def __init__(self):
        self.items = {}  

    def add_item(self, item_name, min_bid):
        self.items[item_name] = {'min_bid': min_bid, 'current_bid': 0, 'highest_bidder': None}

    def place_bid(self, item_name, bidder_name, bid_amount):
        if item_name in self.items:
            item = self.items[item_name]
            if bid_amount >= item['min_bid'] and bid_amount > item['current_bid']:
                item['current_bid'] = bid_amount
                item['highest_bidder'] = bidder_name
                return True
            else:
                return False
        return False

    def get_auction_results(self):
        return self.items

class AuctionSystem:
    def __init__(self, root):
        self.auction = Auction()
        self.root = root
        self.root.title("Online Auction System")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Item Name:").grid(row=0, column=0)
        self.item_name_entry = tk.Entry(self.root)
        self.item_name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Minimum Bid:").grid(row=1, column=0)
        self.min_bid_entry = tk.Entry(self.root)
        self.min_bid_entry.grid(row=1, column=1)

        tk.Button(self.root, text="Add Item", command=self.add_item).grid(row=2, column=1)

        tk.Label(self.root, text="Bidder Name:").grid(row=3, column=0)
        self.bidder_name_entry = tk.Entry(self.root)
        self.bidder_name_entry.grid(row=3, column=1)

        tk.Label(self.root, text="Bid Amount:").grid(row=4, column=0)
        self.bid_amount_entry = tk.Entry(self.root)
        self.bid_amount_entry.grid(row=4, column=1)

        tk.Label(self.root, text="Item to Bid On:").grid(row=5, column=0)
        self.bid_item_entry = tk.Entry(self.root)
        self.bid_item_entry.grid(row=5, column=1)

        tk.Button(self.root, text="Place Bid", command=self.place_bid).grid(row=6, column=1)

        tk.Button(self.root, text="Show Auction Results", command=self.show_results).grid(row=7, column=1)

    def add_item(self):
        item_name = self.item_name_entry.get()
        min_bid = int(self.min_bid_entry.get())
        self.auction.add_item(item_name, min_bid)
        messagebox.showinfo("Info", f"Item '{item_name}' added with a minimum bid of {min_bid}.")

    def place_bid(self):
        item_name = self.bid_item_entry.get()
        bidder_name = self.bidder_name_entry.get()
        bid_amount = int(self.bid_amount_entry.get())
        if self.auction.place_bid(item_name, bidder_name, bid_amount):
            messagebox.showinfo("Success", "Bid placed successfully!")
        else:
            messagebox.showerror("Error", "Bid too low or item does not exist.")

    def show_results(self):
        results = self.auction.get_auction_results()
        result_text = ""
        for item, details in results.items():
            result_text += f"Item: {item}, Highest Bid: {details['current_bid']}, Highest Bidder: {details['highest_bidder']}\n"
        messagebox.showinfo("Auction Results", result_text)

root = tk.Tk()
app = AuctionSystem(root)
root.mainloop()

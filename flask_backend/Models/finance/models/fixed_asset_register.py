import json

class FixedAssetRegister:
    def __init__(self):
        self.assets = []
        self.journal_entries = []

    def add_asset(self, id, asset_name, asset_type, purchase_date, purchase_price, depreciation_rate, depreciation_method, useful_life):
        asset = {
            "id": id,
            "asset_name": asset_name,
            "asset_type": asset_type,
            "purchase_date": purchase_date,
            "purchase_price": purchase_price,
            "depreciation_rate": depreciation_rate,
            "depreciation_method": depreciation_method,
            "useful_life": useful_life,
            "current_value": purchase_price,
            "depreciation_charge": 0.0,
            "accumulated_depreciation": 0.0,
            "net_book_value": purchase_price
        }
        self.assets.append(asset)

    def calculate_depreciation(self):
        for asset in self.assets:
            if asset["depreciation_method"] == "straight_line":
                depreciation_charge = asset["purchase_price"] * (asset["depreciation_rate"] / 100) / asset["useful_life"]
            elif asset["depreciation_method"] == "reducing_balance":
                depreciation_charge = asset["current_value"] * (asset["depreciation_rate"] / 100)
            else:
                raise ValueError("Invalid depreciation method")
            asset["depreciation_charge"] = depreciation_charge
            asset["accumulated_depreciation"] += depreciation_charge
            asset["current_value"] -= depreciation_charge
            asset["net_book_value"] = asset["purchase_price"] - asset["accumulated_depreciation"]

    def create_journal_entry(self, asset_id, date):
        asset = next((asset for asset in self.assets if asset["id"] == asset_id), None)
        if asset:
            journal_entry = {
                "date": date,
                "debit": {
                    "account": "Depreciation Expense",
                    "amount": asset["depreciation_charge"]
                },
                "credit": {
                    "account": "Accumulated Depreciation",
                    "amount": asset["depreciation_charge"]
                },
                "description": f"Depreciation of {asset['asset_name']} for {date}"
            }
            self.journal_entries.append(journal_entry)
            print(f"Journal entry created for asset {asset_id} on {date}")
        else:
            print(f"Asset {asset_id} not found")

    def get_assets(self):
        return self.assets

    def get_journal_entries(self):
        return self.journal_entries

    def to_json(self):
        return json.dumps(self.assets, indent=4)

"""
# Create an instance of the FixedAssetRegister class
register = FixedAssetRegister()

# Add some assets to the register
register.add_asset(1, "Computer", "IT Equipment", "2020-01-01", 1000.00, 20.00, "straight_line", 5)
register.add_asset(2, "Printer", "IT Equipment", "2020-02-01", 500.00, 15.00, "reducing_balance", 3)
register.add_asset(3, "Furniture", "Office Equipment", "2019-03-01", 2000.00, 10.00, "straight_line", 10)
register.add_asset(4, "Vehicle", "Transportation", "2018-04-01", 15000.00, 25.00, "reducing_balance", 5)

# Calculate the depreciation for each asset
register.calculate_depreciation()

# Create journal entries for each asset
register.create_journal_entry(1, "2022-01-01")
register.create_journal_entry(2, "2022-02-01")
register.create_journal_entry(3, "2022-03-01")
register.create_journal_entry(4, "2022-04-01")

# Get the assets and journal entries as JSON strings
assets_json = register.to_json()
journal_entries_json = json.dumps(register.get_journal_entries(), indent=4)

# Print the JSON data
print(assets_json)
print(journal_entries_json)

"""


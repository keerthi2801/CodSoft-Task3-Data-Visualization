import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the cleaned dataset
df = pd.read_csv("cleaned_customer_data.csv")

print("Dataset loaded successfully!")
print(df.head())
plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="Location")

plt.title("Customers by Location")
plt.xlabel("Location")
plt.ylabel("Number of Customers")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
df["PurchaseDate"] = pd.to_datetime(df["PurchaseDate"])

df = df.sort_values("PurchaseDate")
plt.figure(figsize=(10, 5))

plt.plot(
    df["PurchaseDate"],
    df["PurchaseAmount"],
    marker="o"
)

plt.title("Purchase Amount Over Time")
plt.xlabel("Purchase Date")
plt.ylabel("Purchase Amount")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
plt.figure(figsize=(8, 5))

plt.hist(
    df["Age"],
    bins=8,
    edgecolor="black"
)

plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.show()
gender_counts = df["Gender"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    gender_counts,
    labels=gender_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Gender Distribution")

plt.show()
plt.savefig("customers_by_location.png")
plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="Location")

plt.title("Customers by Location")
plt.xlabel("Location")
plt.ylabel("Number of Customers")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("customers_by_location.png")
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# CODSOFT INTERNSHIP - TASK 3
# DATA VISUALIZATION
# ==========================================

# Load dataset
df = pd.read_csv("cleaned_customer_data.csv")

print("Dataset loaded successfully!")
print(df.head())

# Convert PurchaseDate to datetime
df["PurchaseDate"] = pd.to_datetime(df["PurchaseDate"])

# Sort by date
df = df.sort_values("PurchaseDate")


# ==========================================
# 1. BAR CHART - Customers by Location
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="Location")

plt.title("Customers by Location")
plt.xlabel("Location")
plt.ylabel("Number of Customers")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("customers_by_location.png")
plt.close()


# ==========================================
# 2. LINE CHART - Purchase Amount Over Time
# ==========================================

plt.figure(figsize=(10, 5))

plt.plot(
    df["PurchaseDate"],
    df["PurchaseAmount"],
    marker="o"
)

plt.title("Purchase Amount Over Time")
plt.xlabel("Purchase Date")
plt.ylabel("Purchase Amount")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("purchase_amount_over_time.png")
plt.close()


# ==========================================
# 3. HISTOGRAM - Age Distribution
# ==========================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["Age"],
    bins=8,
    edgecolor="black"
)

plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("age_distribution.png")
plt.close()


# ==========================================
# 4. SCATTER PLOT - Age vs Purchase Amount
# ==========================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Age",
    y="PurchaseAmount"
)

plt.title("Age vs Purchase Amount")
plt.xlabel("Age")
plt.ylabel("Purchase Amount")

plt.tight_layout()

plt.savefig("age_vs_purchase.png")
plt.close()


# ==========================================
# 5. PIE CHART - Gender Distribution
# ==========================================

gender_counts = df["Gender"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    gender_counts,
    labels=gender_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Gender Distribution")

plt.savefig("gender_distribution.png")
plt.close()


print("\n======================================")
print("All visualizations created successfully!")
print("======================================")
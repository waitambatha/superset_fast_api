import pandas as pd
from backend.database import SessionLocal
from backend.models import Medicine


async def load_data():
    session = SessionLocal()
    df = pd.read_csv("med.csv")

    for _, row in df.iterrows():
        medicine = Medicine(
            id=row["Medicine_ID"].split("-")[1],
            name=row["Name"],
            type=row["Type"],
            category=row["Category"],
            price=row["Price"],
            stock=row["Stock"],
            manufacturer=row["Manufacturer"],
            expiry_date=row["Expiry_Date"],
            prescription_required=row["Prescription_Required"] == "Yes",
            discount_percentage=row["Discount_Percentage"],
        )
        session.add(medicine)

    await session.commit()
    await session.close()

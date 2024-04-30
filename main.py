from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()
df = pd.read_csv("./Files/kz.csv")

@app.get("/items/user/{user_id}")
def get_pandas_user(user_id: int):
    return df[df.user_id == user_id].to_dict(orient="records")

@app.post("/add-item/")
def add_pandas_command(item: dict):
    global df
    try:
        new_df = pd.DataFrame([item])
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_csv("./Files/kz.csv", index=False)
        return {"message": "Item ajouter!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete-item/{order_id}")
def delete_item(order_id: int):
    global df
    df = df[df.order_id != order_id]
    df.to_csv("./Files/kz.csv", index=False)
    return {"message": "Item supprimer!"}

@app.put("/update-item/{order_id}")
def update_item(order_id: int, item: dict):
    global df
    try:
        for key, value in item.items():
            df.loc[df.order_id == order_id, key] = value
        df.to_csv("./Files/kz.csv", index=False)
        return {"message": "Item modifier!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

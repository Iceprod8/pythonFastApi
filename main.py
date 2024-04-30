from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
import pandas as pd

app = FastAPI()
df = pd.read_csv("./Files/kz.csv")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Fonction de vérification de l'utilisateur
def authenticate_user(token: str = Depends(oauth2_scheme)):
    with open("auth.txt", "r") as f:
        auth_token = f.read().strip()

    if not token or token != auth_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return True


# Route GET pour lire un élément par ID utilisateur
@app.get("/items/user/{user_id}")
def read_item_user(user_id: int, token: str = Depends(oauth2_scheme)):
    authenticate_user(token)
    return df[df.user_id == user_id].to_dict(orient="records")


# Route POST pour ajouter un élément
@app.post("/add-item/")
def add_item(item: dict, token: str = Depends(oauth2_scheme)):
    authenticate_user(token)
    global df
    try:
        new_df = pd.DataFrame([item])
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_csv("./Files/kz.csv", index=False)
        return {"message": "Élément ajouté avec succès!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Route DELETE pour supprimer un élément par ID
@app.delete("/delete-item/{order_id}")
def delete_item(order_id: int, token: str = Depends(oauth2_scheme)):
    authenticate_user(token)
    global df
    df = df[df.order_id != order_id]
    df.to_csv("./Files/kz.csv", index=False)
    return {"message": "Élément supprimé avec succès!"}


# Route PUT pour mettre à jour un élément par ID
@app.put("/update-item/{order_id}")
def update_item(order_id: int, item: dict, token: str = Depends(oauth2_scheme)):
    authenticate_user(token)
    global df
    try:
        for key, value in item.items():
            df.loc[df.order_id == order_id, key] = value
        df.to_csv("./Files/kz.csv", index=False)
        return {"message": "Élément mis à jour avec succès!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

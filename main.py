from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Usuario(BaseModel):
    id: int
    nombre: str
    correo: str


app = FastAPI()

# Simulación de base de datos en memoria
usuarios = {}

@app.post("/usuarios/")
async def crear_usuario(usuario_id: int, usuario: Usuario):
    if usuario_id in usuarios:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    usuarios[usuario_id] = usuario
    return usuarios[usuario_id]

@app.get("/usuarios/{usuario_id}")
async def leer_usuario(usuario_id: int):
    if usuario_id not in usuarios:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuarios[usuario_id]

@app.put("/usuarios/{usuario_id}")
async def actualizar_usuario(usuario_id: int, usuario: Usuario):
    if usuario_id not in usuarios:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuarios[usuario_id] = usuario
    return usuarios[usuario_id]

@app.delete("/usuarios/{usuario_id}")
async def eliminar_usuario(usuario_id: int):
    if usuario_id not in usuarios:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    del usuarios[usuario_id]
    return {"mensaje": "Usuario eliminado"}

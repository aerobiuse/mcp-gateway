from fastapi import APIRouter, Header, HTTPException

router = APIRouter()

@router.get("/tools")
async def list_tools(x_api_key: str = Header(...)):
    if x_api_key != "demo-key-123":
        raise HTTPException(401)
    return {"tools": ["filesystem/list", "calculator/add"]}

@router.post("/tools/{server}/{method}")
async def call_tool(server: str, method: str, payload: dict, x_api_key: str = Header(...)):
    if x_api_key != "demo-key-123":
        raise HTTPException(401)
    return {"result": f"{server}/{method} executed", "data": payload}

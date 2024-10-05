import { config } from "dotenv"
config()
import express from "express"
import * as routes from "./routes"
import cookieParser from "cookie-parser"
const app = express()

app.use(express.json())
app.use(cookieParser());

app.use("/auth", routes.userRoutes)

app.use("*/*", (req,res)=>{
    res.status(404).send("404 Not Found")
})

app.listen(8080, () => {
    console.log("Server is running on port", "8080")
})
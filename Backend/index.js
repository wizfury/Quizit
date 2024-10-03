require("dotenv").config()
const express = require("express")
const app = express()
const print = (req,res,next) => {
    console.log("first")
    res.sendStatus(400)
}
const trial = (endpoint) => {
    return [endpoint, print]
}

app.get(...trial("/"),(req, res) => {
    res.send("Hello World")
})

app.listen(8080, () => {
    console.log("Server is running on port", "8080")
})
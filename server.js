import express from "express";
import { spawn } from "child_process";
const app = express();
const PORT = process.env.PORT || 3001;

app.get("/", function(req, res){
    let process = spawn("python", ["./controllers/app.py","a","b"]);
    process.stdout.on("data", function(data){
        res.send(data.toString());
    })
})


app.listen(PORT, function(){
    console.log(`Server is running on port ${PORT}.`);
});
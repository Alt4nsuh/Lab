const express = require("express");
const dotenv = require("dotenv");
const path = require("path");
const rfs = require("rotating-file-stream"); // version 2.x

const morgan = require("morgan");
const colors = require("colors")

//Import routes
const errorHandler = require("./middleware/error")
const cateRoute = require("./routes/categoreis");
const bookRoute = require("./routes/books");
const logger = require("./middleware/logger");
const connectDB = require("./config/db");

///---------------------------------------------------------------------///

dotenv.config({ path: "config/config.env" });
connectDB();

const accessLogStream = rfs.createStream("access.log", {
  interval: "1d", // rotate daily
  path: path.join(__dirname, "log"),
});

const app = express();


//Body parser == req.body
app.use(express.json())
app.use(logger);
app.use(morgan("combined", { stream: accessLogStream }));
app.use("/api/v1/categoreis", cateRoute);
app.use("/api/v1/books", bookRoute);
app.use(errorHandler)

const server = app.listen(
  process.env.PORT,
  console.log(`Connect to ${process.env.PORT}`)
);

process.on('unhandledRejection',(err, promise)=>{
  console.log(`Error : ${err.message}`.red.underline.bgGray)
  server.close(()=>{
    process.exit(1)
  }) 
})

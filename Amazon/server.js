const express = require("express");
const dotenv = require("dotenv");
var path = require("path");
var rfs = require("rotating-file-stream");
const connectDB = require("./config/db");
const colors = require("colors");
const errorHandler = require("./middleware/error");
var morgan = require("morgan");
const logger = require("./middleware/logger");
const fileupload = require("express-fileupload");
// Router оруулж ирэх
const categoriesRoutes = require("./routes/categories");
const booksRoutes = require("./routes/books");
const usersRoutes = require("./routes/users");
const commentsRoutes = require("./routes/comments");
const injectDb = require("./middleware/injectDb");

// Аппын тохиргоог process.env рүү ачаалах
dotenv.config({ path: "./config/config.env" });

const db = require("./config/db-mysql");

const app = express();

connectDB();

// create a write stream (in append mode)
var accessLogStream = rfs.createStream("access.log", {
  interval: "1d", // rotate daily
  path: path.join(__dirname, "log"),
});

// Body parser
app.use(express.json());
app.use(fileupload());
app.use(logger);
app.use(injectDb(db));
app.use(morgan("combined", { stream: accessLogStream }));
app.use("/api/v1/categories", categoriesRoutes);
app.use("/api/v1/books", booksRoutes);
app.use("/api/v1/users", usersRoutes);
app.use("/api/v1/comments", commentsRoutes);
app.use(errorHandler);

db.user.belongsToMany(db.book, { through: "comment" });
db.book.belongsToMany(db.user, { through: "comment" });
db.category.hasMany(db.book);
db.book.belongsTo(db.category);

db.sequelize
  .sync()
  .then((result) => {
    console.log("sync hiigdlee...");
  })
  .catch((err) => console.log(err));

const server = app.listen(
  process.env.PORT,
  console.log(`Express сэрвэр ${process.env.PORT} порт дээр аслаа... `.rainbow)
);

process.on("unhandledRejection", (err, promise) => {
  console.log(`Алдаа гарлаа : ${err.message}`.underline.red.bold);
  server.close(() => {
    process.exit(1);
  });
});

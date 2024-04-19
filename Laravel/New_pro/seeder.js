const fs = require("fs");
const mongoose = require("mongoose");
const colors = require("colors");
const dotenv = require("dotenv");
const Category = require("./models/Category");
const Book = require("./models/Book");
dotenv.config({ path: "./config/config.env" });

mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const categories = JSON.parse(
  fs.readFileSync(__dirname + "/data/categories.json", "utf-8")
);

const books = JSON.parse(
  fs.readFileSync(__dirname + "/data/book.json", "utf-8")
);

const importDataCategory = async () => {
  try {
    await Category.create(categories);
    await Book.create(books);
    console.log("data import Book")

  } catch (err) {
    console.log(err.message);
  }
};


const deleteDataCategory = async () => {
  try {
    await Category.deleteMany(); 
    await Book.deleteMany(); 
    console.log("data delete Book")

  } catch (err) {
    console.log(err.message);
  }
};


if(process.argv[2]== "-i"){
  importDataCategory()
}else if(process.argv[2]== "-d"){
  deleteDataCategory()
}
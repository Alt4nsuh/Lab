const express = require("express");

const router = express.Router();
const {
  getBooks,
  getCategory,
  createBooks,
  deleteBooks,
  updateBooks,
} = require("../controller/books");

///api/v1/books
router.route("/").get(getBooks);

module.exports = router
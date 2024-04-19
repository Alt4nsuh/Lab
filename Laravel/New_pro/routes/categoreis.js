const express = require("express");

const router = express.Router();
const {
  getCategories,
  getCategory,
  createCategories,
  deleteCategories,
  updateCategories,
} = require("../controller/categoreis");

const {
  getBooks,
} = require("../controller/books");
///api/v1/categoreis
router.route("/").get(getCategories).post(createCategories);
///api/v1/categoreis
router
  .route("/:catId/books").get(getBooks)

router
  .route("/:id/")
  .put(updateCategories)
  .delete(deleteCategories)
  .get(getCategory);

module.exports = router
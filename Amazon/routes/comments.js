const express = require("express");
const router = express.Router();

const { createComment,updateComment} = require("../controller/comments");

//"/api/v1/comments"
router
  .route("/")
  .post(protect, authorize("admin", "operator", "user"), createComment);

router
  .route("/:id")
  .get()
  .put(protect,authorize("admin", "operator", "user"),updateComment)
module.exports = router;

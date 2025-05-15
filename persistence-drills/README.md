# Persistence Drills

This module is all about learning how to **save and manage data** — whether that’s to a file, a database, or somewhere more complex.

### Serialization:

* **Pickle**: Quick and easy way to save Python objects to files and bring them back.
* **JSON/YAML**: Great for human-readable formats. You’ll learn how to serialize and deserialize classes like `Book`, `Car`, and even graphs.
* **Edge Cases**: Handle tricky stuff like skipping sensitive fields, cyclic references, or restoring app/game state.

### SQLite:

* No servers, just a simple `.db` file — perfect for prototyping.
* You'll learn how to:

  * Create tables, insert/read/update/delete data
  * Use classes to wrap DB logic
  * Add searching, validation, transactions, and even CSV export
* Exercises ramp up from basic inserts to real-world use cases like **banking transactions** and **inventory systems**.

### SQLAlchemy + Pydantic:

* This is where the **real-world engineering mindset kicks in**.
* You’ll design models, validate data, handle relationships, and even switch to async programming.
* Topics include:

  * Upserts
  * Schema migrations
  * Data versioning
  * Concurrency
  * Handling binary files
  * Soft deletes
  * Performance testing with millions of rows



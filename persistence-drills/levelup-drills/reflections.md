
### 1. Schema Evolution and Migrations

- **What could go wrong if you applied this change directly?**  
  If we apply the schema change directly (like `ALTER TABLE`) on a live production database, we might lock the table and cause downtime. If something goes wrong or the migration fails halfway, we could corrupt the schema or lose availability.

- **How do production systems manage zero downtime migrations?**  
  In production, we usually add new columns or tables in a backward-compatible way first. Then we deploy code that starts using them. After everything is verified to work, we remove the old ones. This is often called a "3-phase migration" and helps avoid breaking things during deployment.

---

### 2. Model Boundary Enforcement

- **Why is it risky to return raw ORM objects directly?**  
  ORM models are tied to the database schema. If we return them directly, any schema change could unexpectedly affect our API behavior. Also, ORM objects often include lazy-loaded fields or internal methods that shouldn't be exposed.

- **What happens if database schema evolves but external APIs do not?**  
  If the schema evolves but APIs don’t update accordingly, clients might get outdated or inconsistent data. It could also break validation or create security issues if we expose unintended fields.

---

### 3. Idempotent Upserts (Insert or Update)

- **Why are idempotent writes important in distributed systems?**  
  In distributed systems, retries are common due to timeouts or failures. If we don’t make writes idempotent, a retry might create duplicate records or overwrite data incorrectly. Upserts help ensure consistency even if the same request comes multiple times.

- **What if the database doesn't support ON CONFLICT natively?**  
  We can simulate upserts with a transaction: try to insert, and if it fails with a unique constraint error, catch it and run an update instead. This requires careful error handling and concurrency control.

---

### 4. Versioned Data Storage

- **When is it better to version data rather than overwrite it?**  
  It’s better to version data when we need audit history, rollback support, or just want to track changes over time. This is especially useful for compliance or debugging, where knowing “who changed what and when” matters.

---

### 5. Concurrency and Race Condition Management

- **How did you break the system in step 1?**  
  Without transactions, concurrent transfers can read and write overlapping balances, causing lost updates or incorrect totals. For example, two users transferring at the same time might double-spend or cause negative balances.

- **Why is locking tricky in high-concurrency environments?**  
  Locking can easily lead to deadlocks or performance bottlenecks. It’s hard to get right, especially when multiple systems or threads are involved. We have to balance correctness with scalability.

---

### 6. Handling Large Binary Data

- **What are the trade-offs between file system storage and database blobs?**  
  Storing images as BLOBs in the DB keeps everything in one place and is easier to back up. But it can make the database large and slow. Storing files on disk with paths in the DB is faster and more scalable, but harder to manage in distributed setups.

---

### 7. Schema-First vs Code-First Modeling

- **When would we prefer each approach?**  
  Schema-first is great when the schema is defined by another team or regulated (like legacy systems or contracts). Code-first is better for greenfield projects where we control the structure. It's more flexible and fits agile workflows.

---

### 8. Data Lifecycle Management

- **Why do many systems use soft deletes?**
  Soft deletes let us “delete” records without losing them permanently. This is helpful for undo operations, auditing, or restoring accidentally deleted items. It also helps avoid issues with foreign key constraints.

- **What risks exist if we forget to filter them?** 
  If we forget to add `WHERE deleted_at IS NULL`, soft-deleted records can sneak into results. This can confuse users or mess up calculations (e.g. showing deleted products in reports).

---

### 9. Boundary Testing with Large Datasets

- **Why do naive ORM patterns fail at scale?**
    ORMs are convenient, but they’re not optimized for bulk operations. Doing 1 million inserts one-by-one is super slow because each one is its own transaction and DB round-trip.

- **How would we monitor and profile real-world performance?**  
  We can use logging, metrics (like Prometheus), and profiling tools (like `cProfile`, `EXPLAIN ANALYZE`, or database logs). This helps us find bottlenecks and see where time and memory are spent.





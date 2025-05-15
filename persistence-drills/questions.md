### 1. What are transactions?

Transactions in databases are a way to group multiple operations into one unit of work. Think of it as a promise that either all changes will happen, or none of them will. So, if something goes wrong in the middle of the process, the transaction can be "rolled back" to avoid partial changes, keeping the data consistent.

### 2. What are ACID properties?

ACID stands for Atomicity, Consistency, Isolation, and Durability

Atomicity - All operations in a transaction are treated as a single unit. If one fails, the whole transaction fails.
Consistency - The database starts in a valid state and ends in a valid state after the transaction. It ensures rules (like constraints) are followed.
Isolation - Transactions are isolated from each other, meaning one transaction won't affect another until it’s complete.
Durability - Once a transaction is committed, its changes are permanent, even if the system crashes.

### 3. Suppose you do not have transactions. Is that system useful? Why?

Without transactions, things can get messy. Say we are updating two tables: one update happens, but the second one fails. Now we’re left with inconsistent data. So, a system without transactions is less reliable and can lead to data corruption. In short, it's not ideal for most use cases.

### 4. What properties does your file system have?

File systems, while not a database, still have properties. They provide basic storage and retrieval functions but lack things like transactions or ACID properties. The properties could include durability (data stays after a reboot) and consistency (files aren't left in random states after crashes), but they don't offer things like isolation or atomicity like databases do.

### 5. Suppose you do not have "A" in ACID? What happens? When is it ok? Give me a scenario where it is ok.

If we lose Atomicity, we could end up with partially completed operations, which can make our data inconsistent. However, there are cases when it’s okay. For example, if we’re doing a simple operation where partial updates don’t affect overall data integrity (like updating a single counter), atomicity might be less critical.

### 6. Without C in ACID properties

Without consistency, data could become invalid or violate integrity rules (like trying to insert a string where a number is expected). It’s crucial for most systems, but in cases like simple logging systems where no complex rules are enforced, it might not be as critical.

### 7. Without I in ACID properties

Without isolation, transactions could interfere with each other, leading to race conditions or inconsistent results. In a system where only one transaction is allowed to run at a time (like a single-user app), isolation might not be as important. But in multi-user environments, it’s necessary to prevent chaos.

### 8. Without D 

Without durability, the data could disappear after a system crash, leading to potential data loss. In cases where data is not mission-critical (like caching non-essential data), we might survive without durability, but it’s usually a bad idea in any system that relies on preserving information.
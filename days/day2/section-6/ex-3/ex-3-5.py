from pydantic import BaseModel, Field

class Employee(BaseModel):
    """
    Represents an employee in the company.
    """
    employee_id: int = Field(..., description="Unique employee identifier")
    department: str = Field(..., description="Department the employee belongs to")
    is_active: bool = Field(..., description="Indicates if the employee is currently active")

e = Employee(employee_id=10, department="Engineering", is_active=True)
print(e)

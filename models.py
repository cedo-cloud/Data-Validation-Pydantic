from datetime import date
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, EmailStr, Field

class Department(str, Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"

class Employee(BaseModel):
    employee_id: UUID = Field(default_factory=uuid4)
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr                 # email validation
    date_of_birth: date
    salary: float = Field(gt=0)
    department: Department
    benefits: bool


# for field, default_factory = generating default values.
             # frozen = is a boolean(is set to True, the entire model cannot be changed later)
             #min_length, max_length = minimum/maximum length of strings.
             # gt = short for "greater than e.g. gt=5".
             #repr = is a boolean determining whether a field will be seen during print.(useful for concealing sensitive data)
             # pattern = ensures a field matchesa specific regex pattern eg  pattern=r"^\+?1?\d{9,15}$" for phone numbers.
             #alias = to assign alias to your field(alernative name)

            
#field_validator --> allows you to write custom functions that validate field values beyond the basic constraints. eg age, name etc...

#BaseModel --> validates data, serialization(.model_dump, .model_dump_json)


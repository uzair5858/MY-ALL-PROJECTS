from pydantic import basemodel , fields 

class employee (basemodel):
    id: int 
    name: str = field(
        ... ,
        min_length = 3 ,
        max_length = 50 ,
        description = "employee name" , 
        example = "hitesh chaudary"
    )
    department: optional[str] = 'genral'
    salary: float = field (... , ge = 10)
    
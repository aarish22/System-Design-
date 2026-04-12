// composition in golang

package UML

import "fmt"
type Employee struct {
	ID   int
	Name string
}

type Company struct {
	Name      string
	Employees []*Employee  // Aggregation 
}


type Engine struct {
    Power int
}

func (e Engine) Start() {
    fmt.Println("Engine started")
}

type Car struct {
    Engine
    Brand string
}

func main() {
    c := Car{Engine: Engine{Power: 150}, Brand: "Toyota"}
    c.Start() 

    e1 := &Employee{ID: 1, Name: "Hinata"}
	e2 := &Employee{ID: 2, Name: "Rimuru"}


	company := Company{
		Name:      "TechCorp",
		Employees: []*Employee{e1, e2},
	}

	
	fmt.Println("Company:", company.Name)
	for _, emp := range company.Employees {
		fmt.Println("Employee:", emp.Name)
	}
}
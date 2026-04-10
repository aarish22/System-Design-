// composition in golang

package UML

import "fmt"

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
}
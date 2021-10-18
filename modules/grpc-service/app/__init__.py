syntax = "proto3"

message PersonMessage{
    int id = 1;
    string first_name = 2;
    string last_name = 3;
    string company_name = 4;
}

message Empyt{}

message PersonMessageList{
    repeated PersonMessage persons = 1;
}

service PersonService{
    rpc Get(Empty) return (PersonMessageList);
}
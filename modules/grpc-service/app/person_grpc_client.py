import grpc
import person_pb2
import person_pb2_grpc

print("Requesting persons...")


channel = grpc.insecure_channel("127.0.0.1:30007")
stub = person_pb2_grpc.PersonServiceStub(channel)

response = stub.Get(person_pb2.Empty())

print(response)
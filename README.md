# Forked Repo Usage for Osmosis
* Checkout osmosis branch
```shell
git checkout chain/osmosis
```
* Install libraries first
```shell
pip install -r requirements.txt
```
## Aggregate
* Download proto files from github
```shell
python aggregate.py osmosis
```
## Compile
* generate *_pb.py files
```shell
python compile.py
```

# Osmosis Protobuf
This repository contains the whole osmosis protobuf files compiled for python and ready to use with grpc. Please use the according .proto file as documentation for each python file.

## Installation

You can install this package directly from the repository by using:

```
python -m pip install osmosis-protobuf
```

## Usage

The following code snippet will query the balances for the address `osmo15hzhcvgs2ljfng6unghvr5l32prwqdyq4aguxn`. The according query.proto file in the bank subdirectory contains the Request and the Response for this request. The details for the response are defined in `QueryAllBalancesResponse`. It contains the balances and pagination attribute which can be accessed as shown in the example below.

```python
import grpc
import osmosis_protobuf.cosmos.bank.v1beta1.query_pb2_grpc as query_pb2_grpc
import osmosis_protobuf.cosmos.bank.v1beta1.query_pb2 as query_pb2

host = "osmosis.strange.love"
port = "9090"

c = grpc.insecure_channel(f'{host}:{port}')
stub = query_pb2_grpc.QueryStub(c)

r = stub.AllBalances(query_pb2.QueryAllBalancesRequest(address="osmo15hzhcvgs2ljfng6unghvr5l32prwqdyq4aguxn"))
print(r.balances)

```

## Build yourself

There are two scripts helping you to fork this repository to work with any cosmos based coin.

Addititional Requirements:

1. `grpcio-tools`
2. `grpclib`
3. `GitPython`
4. `protoletariat`

Steps:

1. Create a config in `configs` and take a existing one as example
2. Run the `aggregate.py` file with your filename without `.json` (Example `python aggregate.py cosmos`)
3. Run the `compile.py` to compile all your files to protobuf
4. Build your package. You're done!

## Protobuf compilation

The files are compiled using the `grpc_tools.protoc` command from the [grpcio-tools](https://pypi.org/project/grpcio-tools/) library.
To compile a .proto file manually use following command:

```
python -m grpc_tools.protoc -I <absolute path to project root> --python_out=. --grpc_python_out=. --grpclib_python_out=. <absolute path to .proto file>
```

After compiling all the files with protoc you need to fix the imports by using [protoletariat](https://github.com/cpcloud/protoletariat)

Note:

- The --grpc_python_out=. and --grpclib_python_out=. is only needed when compiling a query.proto file as these define the actual grpc query
- To compile the whole project it is favorable to match all proto files by using `*.proto` instead of each individual file. You can also match the whole folders to compile multiple folders at the same time. Not that the folders might contain sub-folders.

## Other Cosmos based coins

Currently following coins are maintained by me:
* Cosmos (branch: ``main``)
* Osmosis (this branch)

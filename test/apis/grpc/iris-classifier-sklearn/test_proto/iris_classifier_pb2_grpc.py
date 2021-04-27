# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import iris_classifier_pb2 as iris__classifier__pb2


class HandlerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Predict = channel.unary_unary(
            "/iris_classifier.Handler/Predict",
            request_serializer=iris__classifier__pb2.Sample.SerializeToString,
            response_deserializer=iris__classifier__pb2.Response.FromString,
        )


class HandlerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Predict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_HandlerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Predict": grpc.unary_unary_rpc_method_handler(
            servicer.Predict,
            request_deserializer=iris__classifier__pb2.Sample.FromString,
            response_serializer=iris__classifier__pb2.Response.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "iris_classifier.Handler", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Handler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Predict(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/iris_classifier.Handler/Predict",
            iris__classifier__pb2.Sample.SerializeToString,
            iris__classifier__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

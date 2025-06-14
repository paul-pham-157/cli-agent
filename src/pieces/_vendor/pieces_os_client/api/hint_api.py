# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic.v1 import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic.v1 import Field, StrictStr

from typing import Optional

from pieces._vendor.pieces_os_client.models.hint import Hint
from pieces._vendor.pieces_os_client.models.seeded_score_increment import SeededScoreIncrement

from pieces._vendor.pieces_os_client.api_client import ApiClient
from pieces._vendor.pieces_os_client.api_response import ApiResponse
from pieces._vendor.pieces_os_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class HintApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def hint_associate_asset(self, hint : Annotated[StrictStr, Field(..., description="This is a specific hint uuid")], asset : Annotated[StrictStr, Field(..., description="The id (uuid) of the asset that you are trying to access.")], **kwargs) -> None:  # noqa: E501
        """/hint/{hint}/assets/associate/{asset} [POST]  # noqa: E501

        associates a hint and an asset. It performs the same action as the asset equivalent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.hint_associate_asset(hint, asset, async_req=True)
        >>> result = thread.get()

        :param hint: This is a specific hint uuid (required)
        :type hint: str
        :param asset: The id (uuid) of the asset that you are trying to access. (required)
        :type asset: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the hint_associate_asset_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.hint_associate_asset_with_http_info(hint, asset, **kwargs)  # noqa: E501

    @validate_arguments
    def hint_associate_asset_with_http_info(self, hint : Annotated[StrictStr, Field(..., description="This is a specific hint uuid")], asset : Annotated[StrictStr, Field(..., description="The id (uuid) of the asset that you are trying to access.")], **kwargs) -> ApiResponse:  # noqa: E501
        """/hint/{hint}/assets/associate/{asset} [POST]  # noqa: E501

        associates a hint and an asset. It performs the same action as the asset equivalent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.hint_associate_asset_with_http_info(hint, asset, async_req=True)
        >>> result = thread.get()

        :param hint: This is a specific hint uuid (required)
        :type hint: str
        :param asset: The id (uuid) of the asset that you are trying to access. (required)
        :type asset: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'hint',
            'asset'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hint_associate_asset" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['hint'] is not None:
            _path_params['hint'] = _params['hint']

        if _params['asset'] is not None:
            _path_params['asset'] = _params['asset']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # authentication setting
        _auth_settings = ['application']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/hint/{hint}/assets/associate/{asset}', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def hint_disassociate_asset(self, hint : Annotated[StrictStr, Field(..., description="This is a specific hint uuid")], asset : Annotated[StrictStr, Field(..., description="The id (uuid) of the asset that you are trying to access.")], **kwargs) -> None:  # noqa: E501
        """/hint/{hint}/assets/disassociate/{asset} [POST]  # noqa: E501

        Disassociates a hint from an asset. It performs the same action as the asset equivalent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.hint_disassociate_asset(hint, asset, async_req=True)
        >>> result = thread.get()

        :param hint: This is a specific hint uuid (required)
        :type hint: str
        :param asset: The id (uuid) of the asset that you are trying to access. (required)
        :type asset: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the hint_disassociate_asset_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.hint_disassociate_asset_with_http_info(hint, asset, **kwargs)  # noqa: E501

    @validate_arguments
    def hint_disassociate_asset_with_http_info(self, hint : Annotated[StrictStr, Field(..., description="This is a specific hint uuid")], asset : Annotated[StrictStr, Field(..., description="The id (uuid) of the asset that you are trying to access.")], **kwargs) -> ApiResponse:  # noqa: E501
        """/hint/{hint}/assets/disassociate/{asset} [POST]  # noqa: E501

        Disassociates a hint from an asset. It performs the same action as the asset equivalent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.hint_disassociate_asset_with_http_info(hint, asset, async_req=True)
        >>> result = thread.get()

        :param hint: This is a specific hint uuid (required)
        :type hint: str
        :param asset: The id (uuid) of the asset that you are trying to access. (required)
        :type asset: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'hint',
            'asset'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hint_disassociate_asset" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['hint'] is not None:
            _path_params['hint'] = _params['hint']

        if _params['asset'] is not None:
            _path_params['asset'] = _params['asset']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # authentication setting
        _auth_settings = ['application']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/hint/{hint}/assets/disassociate/{asset}', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def hint_scores_increment(self, hint : Annotated[StrictStr, Field(..., description="This is a specific hint uuid")], seeded_score_increment : Optional[SeededScoreIncrement] = None, **kwargs) -> None:  # noqa: E501
        """'/hint/{hint}/scores/increment' [POST]  # noqa: E501

        This will take in a SeededScoreIncrement and will increment the material relative to the incoming body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.hint_scores_increment(hint, seeded_score_increment, async_req=True)
        >>> result = thread.get()

        :param hint: This is a specific hint uuid (required)
        :type hint: str
        :param seeded_score_increment:
        :type seeded_score_increment: SeededScoreIncrement
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the hint_scores_increment_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.hint_scores_increment_with_http_info(hint, seeded_score_increment, **kwargs)  # noqa: E501

    @validate_arguments
    def hint_scores_increment_with_http_info(self, hint : Annotated[StrictStr, Field(..., description="This is a specific hint uuid")], seeded_score_increment : Optional[SeededScoreIncrement] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """'/hint/{hint}/scores/increment' [POST]  # noqa: E501

        This will take in a SeededScoreIncrement and will increment the material relative to the incoming body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.hint_scores_increment_with_http_info(hint, seeded_score_increment, async_req=True)
        >>> result = thread.get()

        :param hint: This is a specific hint uuid (required)
        :type hint: str
        :param seeded_score_increment:
        :type seeded_score_increment: SeededScoreIncrement
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'hint',
            'seeded_score_increment'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hint_scores_increment" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['hint'] is not None:
            _path_params['hint'] = _params['hint']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['seeded_score_increment'] is not None:
            _body_params = _params['seeded_score_increment']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['application']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/hint/{hint}/scores/increment', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def hint_specific_hint_snapshot(self, hint : Annotated[StrictStr, Field(..., description="This is a specific hint uuid")], **kwargs) -> Hint:  # noqa: E501
        """/hint/{hint} [POST]  # noqa: E501

        This will get a snapshot of a specific hint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.hint_specific_hint_snapshot(hint, async_req=True)
        >>> result = thread.get()

        :param hint: This is a specific hint uuid (required)
        :type hint: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Hint
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the hint_specific_hint_snapshot_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.hint_specific_hint_snapshot_with_http_info(hint, **kwargs)  # noqa: E501

    @validate_arguments
    def hint_specific_hint_snapshot_with_http_info(self, hint : Annotated[StrictStr, Field(..., description="This is a specific hint uuid")], **kwargs) -> ApiResponse:  # noqa: E501
        """/hint/{hint} [POST]  # noqa: E501

        This will get a snapshot of a specific hint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.hint_specific_hint_snapshot_with_http_info(hint, async_req=True)
        >>> result = thread.get()

        :param hint: This is a specific hint uuid (required)
        :type hint: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Hint, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'hint'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hint_specific_hint_snapshot" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['hint'] is not None:
            _path_params['hint'] = _params['hint']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # authentication setting
        _auth_settings = ['application']  # noqa: E501

        _response_types_map = {
            '200': "Hint",
            '500': "str",
        }

        return self.api_client.call_api(
            '/hint/{hint}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def hint_update(self, hint : Optional[Hint] = None, **kwargs) -> Hint:  # noqa: E501
        """/hint/update [POST]  # noqa: E501

        This will update a specific hint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.hint_update(hint, async_req=True)
        >>> result = thread.get()

        :param hint:
        :type hint: Hint
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Hint
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the hint_update_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.hint_update_with_http_info(hint, **kwargs)  # noqa: E501

    @validate_arguments
    def hint_update_with_http_info(self, hint : Optional[Hint] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/hint/update [POST]  # noqa: E501

        This will update a specific hint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.hint_update_with_http_info(hint, async_req=True)
        >>> result = thread.get()

        :param hint:
        :type hint: Hint
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Hint, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'hint'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hint_update" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['hint'] is not None:
            _body_params = _params['hint']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['application']  # noqa: E501

        _response_types_map = {
            '200': "Hint",
            '500': "str",
        }

        return self.api_client.call_api(
            '/hint/update', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

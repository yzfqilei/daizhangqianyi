#!/usr/bin/python
# coding:utf-8
from core.checkresult import check_codes_msg, check_datas
from core.rest_client import RestClient
from common.write_data import WriteFileData
from core.common_params import get_common_params
import json, sys, time, random
import allure
import pytest
from common import path_conf
from core import result_base
from common import get_root_url
from common.mysql_operate import db

reportpath = path_conf.REPORT_PATH
wd = WriteFileData()
rooturl = get_root_url.get_root_urls()
result = result_base.ResultBase()
a = RestClient(rooturl)


@pytest.mark.usefixtures("is_login")
@allure.feature("流程管理测试用例")
class Test_process_manage():
    #查询方法，创建完之后返回流程id等信息
    def search_process(self, name):
        url = f'/apis/crm-workflow/workflow/procDefs?name={name}&type&status&formId&pageIndex=1&pageSize=10'
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=url, method=method, headers=headers)
        dict = json.loads(res.text)
        data = dict['data']
        list = data['list']
        id_dict = list[0]
        id = id_dict['id']
        print('----------查询成功！')
        return id

    @allure.story("创建审批流")
    def test_01create_approval_flow001(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        data={"procDef":{"procDefId":None,"bpmnXml":"<definitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:flowable=\"http://flowable.org/bpmn\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" typeLanguage=\"http://www.w3.org/2001/XMLSchema\" expressionLanguage=\"http://www.w3.org/1999/XPath\" targetNamespace=\"http://www.flowable.org/processdef\"><process id=\"flowable-1601172946156\" name=\"approval_flow\" isExecutable=\"true\"><extensionElements/><startEvent id=\"node-start\" name=\"开始\" flowable:initiator=\"starter\"></startEvent><endEvent id=\"node-end\" name=\"结束\"></endEvent><userTask id=\"input-6e898487\" name=\"node\" flowable:formKey=\"\"><extensionElements></extensionElements></userTask><sequenceFlow id=\"line-84b60c88\" sourceRef=\"node-start\" targetRef=\"input-6e898487\"></sequenceFlow><sequenceFlow id=\"line-9d70bfb8\" sourceRef=\"input-6e898487\" targetRef=\"node-end\"></sequenceFlow></process><bpmndi:BPMNDiagram id=\"BPMNDiagram_flowable-1601172946156\"><bpmndi:BPMNPlane bpmnElement=\"flowable-1601172946156\" id=\"BPMNPlane_flowable-1601172946156\"><bpmndi:BPMNShape bpmnElement=\"input-6e898487\" id=\"BPMNShape_input-6e898487\"><omgdc:Bounds height=\"35\" width=\"60\" x=\"239.015625\" y=\"72\"></omgdc:Bounds></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"node-start\" id=\"BPMNShape_node-start\"><omgdc:Bounds height=\"50\" width=\"50\" x=\"50\" y=\"50\"></omgdc:Bounds></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"node-end\" id=\"BPMNShape_node-end\"><omgdc:Bounds height=\"50\" width=\"50\" x=\"650\" y=\"480\"></omgdc:Bounds></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement=\"line-84b60c88\" id=\"BPMNEdge_line-84b60c88\"><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement=\"line-9d70bfb8\" id=\"BPMNEdge_line-9d70bfb8\"><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint></bpmndi:BPMNEdge></bpmndi:BPMNPlane></bpmndi:BPMNDiagram></definitions>","formId":"756585727382392840","name":"approval_flow","ruleCyclePeriod":"","ruleCycleTime":"undefined undefined  * * ?","ruleType":0,"status":0,"type":0,"pushFlag":0},"procNodes":[{"assignee":"","assigneeType":-1,"formId":"756585727382392840","name":"node","formLayoutCode":"","pushMsg":0,"taskDefKey":"input-6e898487","id":"","sequence":0}],"procMsg":{"assignee":"","assigneeType":0}}
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=data, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("创建工作流")
    def test_02create_work_flow002(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        data={"procDef":{"procDefId":None,"bpmnXml":"<definitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:flowable=\"http://flowable.org/bpmn\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" typeLanguage=\"http://www.w3.org/2001/XMLSchema\" expressionLanguage=\"http://www.w3.org/1999/XPath\" targetNamespace=\"http://www.flowable.org/processdef\"><process id=\"flowable-1601172398382\" name=\"work_flow\" isExecutable=\"true\"><extensionElements/><startEvent id=\"node-start\" name=\"开始\" flowable:initiator=\"starter\"></startEvent><endEvent id=\"node-end\" name=\"结束\"></endEvent><userTask id=\"input-9f2f8cd8\" name=\"node\" flowable:formKey=\"756585727382392834\" flowable:candidateGroups=\"r_756585370497454081\"><extensionElements></extensionElements></userTask><sequenceFlow id=\"line-f9aacee4\" sourceRef=\"node-start\" targetRef=\"input-9f2f8cd8\"></sequenceFlow><sequenceFlow id=\"line-9ca1f0f1\" sourceRef=\"input-9f2f8cd8\" targetRef=\"node-end\"></sequenceFlow></process><bpmndi:BPMNDiagram id=\"BPMNDiagram_flowable-1601172398382\"><bpmndi:BPMNPlane bpmnElement=\"flowable-1601172398382\" id=\"BPMNPlane_flowable-1601172398382\"><bpmndi:BPMNShape bpmnElement=\"input-9f2f8cd8\" id=\"BPMNShape_input-9f2f8cd8\"><omgdc:Bounds height=\"35\" width=\"60\" x=\"216.015625\" y=\"75\"></omgdc:Bounds></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"node-start\" id=\"BPMNShape_node-start\"><omgdc:Bounds height=\"50\" width=\"50\" x=\"50\" y=\"50\"></omgdc:Bounds></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"node-end\" id=\"BPMNShape_node-end\"><omgdc:Bounds height=\"50\" width=\"50\" x=\"650\" y=\"480\"></omgdc:Bounds></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement=\"line-f9aacee4\" id=\"BPMNEdge_line-f9aacee4\"><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement=\"line-9ca1f0f1\" id=\"BPMNEdge_line-9ca1f0f1\"><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint></bpmndi:BPMNEdge></bpmndi:BPMNPlane></bpmndi:BPMNDiagram></definitions>","formId":"756585727382392834","name":"work_flow","ruleCyclePeriod":"","ruleCycleTime":"undefined undefined  * * ?","ruleType":0,"status":0,"type":1,"pushFlag":0},"procNodes":[{"isBack":0,"assignee":"756585370497454081","assigneeType":5,"formId":"756585727382392834","name":"node","formLayoutCode":"edit","pushMsg":0,"taskDefKey":"input-9f2f8cd8","id":"","sequence":0}],"procMsg":{"assignee":"","assigneeType":0}}
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=data, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("查询流程work_flow")
    def test_03search_process003(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)

        # 由于创建接口不返回流程id，因此此处需要将id返回写入yaml文档中
        id = Test_process_manage.search_process(self, name='work_flow')
        data = {'totalCount': 1, 'pageSize': 10, 'currPage': 1, 'list': [{'id': id, 'name': 'work_flow'}]}
        expectresult = {'code': 0, 'msg': None, 'data': data}
        wd.write_yaml(yaml_path, func_name, 'expectresult', expectresult)

        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("过滤所有类型流程")
    def test_04screen_all004(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        response_str = str(res.text)
        for d in yamlvalue['expectresult']['data']:
            pytest.assume(d in response_str)

    @allure.story("过滤审批流")
    def test_05screen_approval_flow005(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        response_str = str(res.text)
        for d in yamlvalue['expectresult']['data']:
            pytest.assume(d in response_str)

    @allure.story("过滤工作流")
    def test_06screen_work_folw006(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        response_str = str(res.text)
        for d in yamlvalue['expectresult']['data']:
            pytest.assume(d in response_str)

    @allure.story("停用工作流和审批流")
    def test_07deactive_process007(self):
        func_name = sys._getframe().f_code.co_name
        approval_id=Test_process_manage.search_process(self,name='approval_flow')
        work_id = Test_process_manage.search_process(self, name='work_flow')
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        url=csurl+str(approval_id)+','+str(work_id)+'/disable'
        res = a.request(url=url, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("过滤停用流程")
    def test_08screen_status_deactive008(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("启用工作流和审批流")
    def test_09active_process009(self):
        func_name = sys._getframe().f_code.co_name
        approval_id=Test_process_manage.search_process(self,name='approval_flow')
        work_id = Test_process_manage.search_process(self, name='work_flow')
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        url=csurl+str(approval_id)+','+str(work_id)+'/enable'
        res = a.request(url=url, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("过滤启用流程")
    def test_10screen_status_active010(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("过滤所有状态的流程")
    def test_11screen_status_all011(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("删除工作流")
    def test_12delete_work_flow012(self):
        func_name = sys._getframe().f_code.co_name
        id = Test_process_manage.search_process(self, name='work_flow')
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        csurl=csurl+id
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("删除审批流")
    def test_13delete_approval_flow013(self):
        func_name = sys._getframe().f_code.co_name
        id = Test_process_manage.search_process(self, name='approval_flow')
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        csurl=csurl+id
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)
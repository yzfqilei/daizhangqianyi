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
        procDefId = id_dict['procDefId']
        print('----------查询成功！')
        return id, procDefId

    def get_process_data(self, name):
        func_name = sys._getframe().f_code.co_name
        data = {"procDefName": name, "pageIndex": 1, "pageSize": 10, "startApplyTime": None, "endApplyTime": None,
                "type": 0}
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=data, headers=headers)
        dict = json.loads(res.text)
        data = dict['data']['list'][0]
        print(type(data),data)
        procInstId = data['procInstId']
        print('----------查询成功！')
        return procInstId


    @allure.story("创建审批流")
    def test001_create_approval_flow(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        data={"procDef":{"procDefId":None,"bpmnXml":"<definitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:flowable=\"http://flowable.org/bpmn\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" typeLanguage=\"http://www.w3.org/2001/XMLSchema\" expressionLanguage=\"http://www.w3.org/1999/XPath\" targetNamespace=\"http://www.flowable.org/processdef\"><process id=\"flowable-1602297919597\" name=\"approval_flow\" isExecutable=\"true\"><extensionElements/><startEvent id=\"node-start\" name=\"开始\" flowable:initiator=\"starter\"></startEvent><endEvent id=\"node-end\" name=\"结束\"></endEvent><userTask id=\"review-252a859f\" name=\"review\" flowable:formKey=\"\" flowable:candidateGroups=\"u_756574317326995456\"><extensionElements></extensionElements></userTask><userTask id=\"input-97814ba8\" name=\"node\" flowable:formKey=\"\"><extensionElements></extensionElements></userTask><sequenceFlow id=\"line-b0c73353\" sourceRef=\"node-start\" targetRef=\"input-97814ba8\"></sequenceFlow><sequenceFlow id=\"line-406f5e6d\" sourceRef=\"input-97814ba8\" targetRef=\"review-252a859f\"></sequenceFlow><sequenceFlow id=\"line-7a5fc671\" sourceRef=\"review-252a859f\" targetRef=\"node-end\"></sequenceFlow></process><bpmndi:BPMNDiagram id=\"BPMNDiagram_flowable-1602297919597\"><bpmndi:BPMNPlane bpmnElement=\"flowable-1602297919597\" id=\"BPMNPlane_flowable-1602297919597\"><bpmndi:BPMNShape bpmnElement=\"review-252a859f\" id=\"BPMNShape_review-252a859f\"><omgdc:Bounds height=\"40\" width=\"60\" x=\"385.015625\" y=\"116.5\"></omgdc:Bounds></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"input-97814ba8\" id=\"BPMNShape_input-97814ba8\"><omgdc:Bounds height=\"35\" width=\"60\" x=\"225.515625\" y=\"95.5\"></omgdc:Bounds></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"node-start\" id=\"BPMNShape_node-start\"><omgdc:Bounds height=\"50\" width=\"50\" x=\"50\" y=\"50\"></omgdc:Bounds></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"node-end\" id=\"BPMNShape_node-end\"><omgdc:Bounds height=\"50\" width=\"50\" x=\"650\" y=\"480\"></omgdc:Bounds></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement=\"line-b0c73353\" id=\"BPMNEdge_line-b0c73353\"><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement=\"line-406f5e6d\" id=\"BPMNEdge_line-406f5e6d\"><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement=\"line-7a5fc671\" id=\"BPMNEdge_line-7a5fc671\"><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint></bpmndi:BPMNEdge></bpmndi:BPMNPlane></bpmndi:BPMNDiagram></definitions>","formId":"756585727382392840","name":"approval_flow","ruleCyclePeriod":"","ruleCycleTime":"undefined undefined  * * ?","ruleType":0,"status":0,"type":0,"pushFlag":0},"procNodes":[{"assignee":"756574317326995456","assigneeType":6,"formId":"756585727382392840","name":"review","formLayoutCode":"kaipiaoshenpi","pushMsg":0,"taskDefKey":"review-252a859f","id":"","sequence":1},{"assignee":"","assigneeType":-1,"formId":"756585727382392840","name":"node","formLayoutCode":"","pushMsg":0,"taskDefKey":"input-97814ba8","id":"","sequence":0}],"procMsg":{"assignee":"756585370497454081","assigneeType":5}}
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=data, headers=headers)
        print(res.text)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)


    @allure.story("创建工作流")
    def test002_create_work_flow(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        data={"procDef":{"procDefId":None,"bpmnXml":"<definitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:flowable=\"http://flowable.org/bpmn\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" typeLanguage=\"http://www.w3.org/2001/XMLSchema\" expressionLanguage=\"http://www.w3.org/1999/XPath\" targetNamespace=\"http://www.flowable.org/processdef\"><process id=\"flowable-1601172398382\" name=\"work_flow\" isExecutable=\"true\"><extensionElements/><startEvent id=\"node-start\" name=\"开始\" flowable:initiator=\"starter\"></startEvent><endEvent id=\"node-end\" name=\"结束\"></endEvent><userTask id=\"input-9f2f8cd8\" name=\"node\" flowable:formKey=\"756585727382392834\" flowable:candidateGroups=\"r_756585370497454081\"><extensionElements></extensionElements></userTask><sequenceFlow id=\"line-f9aacee4\" sourceRef=\"node-start\" targetRef=\"input-9f2f8cd8\"></sequenceFlow><sequenceFlow id=\"line-9ca1f0f1\" sourceRef=\"input-9f2f8cd8\" targetRef=\"node-end\"></sequenceFlow></process><bpmndi:BPMNDiagram id=\"BPMNDiagram_flowable-1601172398382\"><bpmndi:BPMNPlane bpmnElement=\"flowable-1601172398382\" id=\"BPMNPlane_flowable-1601172398382\"><bpmndi:BPMNShape bpmnElement=\"input-9f2f8cd8\" id=\"BPMNShape_input-9f2f8cd8\"><omgdc:Bounds height=\"35\" width=\"60\" x=\"216.015625\" y=\"75\"></omgdc:Bounds></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"node-start\" id=\"BPMNShape_node-start\"><omgdc:Bounds height=\"50\" width=\"50\" x=\"50\" y=\"50\"></omgdc:Bounds></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"node-end\" id=\"BPMNShape_node-end\"><omgdc:Bounds height=\"50\" width=\"50\" x=\"650\" y=\"480\"></omgdc:Bounds></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement=\"line-f9aacee4\" id=\"BPMNEdge_line-f9aacee4\"><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement=\"line-9ca1f0f1\" id=\"BPMNEdge_line-9ca1f0f1\"><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint><omgdi:waypoint x=\"0\" y=\"0\"></omgdi:waypoint></bpmndi:BPMNEdge></bpmndi:BPMNPlane></bpmndi:BPMNDiagram></definitions>","formId":"756585727382392834","name":"work_flow","ruleCyclePeriod":"","ruleCycleTime":"undefined undefined  * * ?","ruleType":0,"status":0,"type":1,"pushFlag":0},"procNodes":[{"isBack":0,"assignee":"756585370497454081","assigneeType":5,"formId":"756585727382392834","name":"node","formLayoutCode":"edit","pushMsg":0,"taskDefKey":"input-9f2f8cd8","id":"","sequence":0}],"procMsg":{"assignee":"","assigneeType":0}}
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json=data, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("查询流程work_flow")
    def test003_search_process(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)

        # 由于创建接口不返回流程id，因此此处需要将id返回写入yaml文档中
        id, procDefId = Test_process_manage.search_process(self, name='work_flow')
        data = {'totalCount': 1, 'pageSize': 10, 'currPage': 1, 'list': [{'id': id, 'name': 'work_flow'}]}
        expectresult = {'code': 0, 'msg': None, 'data': data}
        wd.write_yaml(yaml_path, func_name, 'expectresult', expectresult)

        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("过滤所有类型流程")
    def test004_screen_all(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        response_str = str(res.text)
        for d in yamlvalue['expectresult']['data']:
            pytest.assume(d in response_str)

    @allure.story("过滤审批流")
    def test005_screen_approval_flow(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        response_str = str(res.text)
        for d in yamlvalue['expectresult']['data']:
            pytest.assume(d in response_str)

    @allure.story("过滤工作流")
    def test006_screen_work_folw(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        response_str = str(res.text)
        for d in yamlvalue['expectresult']['data']:
            pytest.assume(d in response_str)

    @allure.story("停用工作流和审批流")
    def test007_deactive_process(self):
        func_name = sys._getframe().f_code.co_name
        approval_id, procDefId=Test_process_manage.search_process(self,name='approval_flow')
        work_id, procDefId = Test_process_manage.search_process(self, name='work_flow')
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        url=csurl+str(approval_id)+','+str(work_id)+'/disable'
        res = a.request(url=url, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("过滤停用流程")
    def test008_screen_status_deactive(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)
        pytest.assume('approval_flow' in res.text)
        pytest.assume('work_flow' in res.text)

    @allure.story("启用工作流和审批流")
    def test009_active_process(self):
        func_name = sys._getframe().f_code.co_name
        approval_id, procDefId=Test_process_manage.search_process(self,name='approval_flow')
        work_id, procDefId= Test_process_manage.search_process(self, name='work_flow')
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        url=csurl+str(approval_id)+','+str(work_id)+'/enable'
        res = a.request(url=url, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("过滤启用流程")
    def test010_screen_status_active(self):
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        pytest.assume('approval_flow' in res.text)
        pytest.assume('work_flow' in res.text)

    # @allure.story("过滤所有状态的流程")
    # def test011_screen_status_all(self):
    #     func_name = sys._getframe().f_code.co_name
    #     csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
    #     a = RestClient(rooturl)
    #     res = a.request(url=csurl, method=method, headers=headers)
    #     check_codes_msg(res, yamlvalue, mainkey)
    #     pytest.assume('approval_flow' in res.text)
    #     pytest.assume('work_flow' in res.text)
    #     pytest.assume('跟进记录' in res.text)
    #     pytest.assume('开票申请' in res.text)

# 审批菜单中的相关用例
    # -------begin-------
    @allure.story("开始审批")
    def test012_start_approval(self):
        func_name = sys._getframe().f_code.co_name
        approval_id, procDefId = Test_process_manage.search_process(self, name='approval_flow')
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        url = csurl+str(procDefId)+'/start'
        res = a.request(url=url, method=method, json=yamlvalue['data'], headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)
    #审批工作流难点：无法获取任务id，因为任务ID是点击具体的流程后生成的
    # @allure.story("审批同意")
    #def test013_agree_approval(self):
        # func_name = sys._getframe().f_code.co_name
        # approval_id, procDefId = Test_process_manage.search_process(self, name='approval_flow')
        # csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        # a = RestClient(rooturl)
        # url = csurl+str(procDefId)+'/start'
        # res = a.request(url=url, method=method, json=yamlvalue['data'], headers=headers)
        # check_codes_msg(res, yamlvalue, mainkey)
        # check_datas(res, yamlvalue)
    # -------over-------


    @allure.story("删除工作流")
    def test012_delete_work_flow(self):
        func_name = sys._getframe().f_code.co_name
        id, procDefId = Test_process_manage.search_process(self, name='work_flow')
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        csurl=csurl+id
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)

    @allure.story("删除审批流")
    def test013_delete_approval_flow(self):
        func_name = sys._getframe().f_code.co_name
        id, procDefId = Test_process_manage.search_process(self, name='approval_flow')
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        a = RestClient(rooturl)
        csurl=csurl+id
        res = a.request(url=csurl, method=method, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)



    def test014_delete_approval_flow_data(self):
        procDefId = Test_process_manage.get_process_data(self,'approval_flow')
        func_name = sys._getframe().f_code.co_name
        csurl, method, headers, yamlvalue, yaml_path, mainkey = get_common_params('process_manage.yaml', func_name)
        data = {"deleteReason":"","procInsId":[procDefId]}
        a = RestClient(rooturl)
        res = a.request(url=csurl, method=method, json= data, headers=headers)
        check_codes_msg(res, yamlvalue, mainkey)
        check_datas(res, yamlvalue)
        #核实删除结果在查询下
        try:
            result = Test_process_manage.get_process_data(self, 'approval_flow')
        except IndexError as e:
            print('数据为空，删除成功！')
        else:
            print('删除失败！')


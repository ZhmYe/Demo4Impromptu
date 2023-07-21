(function(){var t={7186:function(t,e,i){"use strict";var a=i(6369),n=function(){var t=this,e=t._self._c;return e("div",{staticStyle:{width:"100%",display:"flex","margin-top":"20px","margin-left":"100px","border-bottom":"1px solid lightgray","border-right":"1px solid lightgray"},attrs:{id:"app"}},[e("div",{staticClass:"sidebar",staticStyle:{width:"250px",position:"relative"}},[e("div",{staticStyle:{width:"95%","font-size":"xx-large","font-weight":"700","text-align":"center"}},[t._v("ChainDash")]),e("div",{staticClass:"sidebar-form"},[e("div",{staticClass:"sidebar-title"},[t._v("Address")]),t._l(t.accounts,(function(i,a){return e("div",{key:a,staticStyle:{display:"flex","margin-top":"5px"}},[e("div",[e("el-input",{style:t.getInputStyle(),model:{value:t.accounts[a],callback:function(e){t.$set(t.accounts,a,e)},expression:"accounts[index]"}})],1),e("div",{staticStyle:{height:"40px","line-height":"40px","align-items":"center"}},[e("el-button",{directives:[{name:"show",rawName:"v-show",value:t.accounts.length>1,expression:"accounts.length > 1"}],attrs:{type:"danger",icon:"el-icon-delete",circle:"",size:"mini"},on:{click:function(e){return t.deleteAccount(e,a)}}})],1)])})),e("div",{staticStyle:{"margin-top":"5px","text-align":"center",width:"90%"}},[e("el-button",{attrs:{icon:"el-icon-plus",circle:"",size:"mini"},on:{click:function(e){return t.addAccount(e)}}})],1),e("div",{staticClass:"sidebar-title",staticStyle:{"margin-top":"5px"}},[t._v("K-hop Steps")]),e("el-input",{staticStyle:{width:"200px"},model:{value:t.jump,callback:function(e){t.jump=e},expression:"jump"}}),e("div",{staticClass:"sidebar-title"},[t._v("Query Window")]),e("div",{staticClass:"sidebar-subtitle"},[t._v("Start Block")]),e("el-input",{staticStyle:{width:"200px"},model:{value:t.MinBlocknumber,callback:function(e){t.MinBlocknumber=e},expression:"MinBlocknumber"}}),e("div",{staticClass:"sidebar-subtitle"},[t._v("End Block")]),e("el-input",{staticStyle:{width:"200px"},model:{value:t.MaxBlocknumber,callback:function(e){t.MaxBlocknumber=e},expression:"MaxBlocknumber"}}),e("div",{staticClass:"sidebar-title"},[t._v("Contract Address")]),t._l(t.contracts,(function(i,a){return e("div",{key:a,staticStyle:{display:"flex","margin-top":"5px"}},[t._m(0,!0),e("div",[e("el-input",{style:t.getcontractsInputStyle(),model:{value:t.contracts[a],callback:function(e){t.$set(t.contracts,a,e)},expression:"contracts[index]"}})],1),e("div",{staticStyle:{height:"40px","line-height":"40px","align-items":"center"}},[e("el-button",{directives:[{name:"show",rawName:"v-show",value:t.contracts.length>1,expression:"contracts.length > 1"}],attrs:{type:"danger",icon:"el-icon-delete",circle:"",size:"mini"},on:{click:function(e){return t.deleteContract(e,a)}}})],1)])})),e("div",{staticStyle:{"margin-top":"5px","text-align":"center",width:"100%","margin-left":"35px"}},[e("el-button",{attrs:{icon:"el-icon-plus",circle:"",size:"mini"},on:{click:function(e){return t.addContract(e)}}}),e("el-checkbox",{staticStyle:{"margin-left":"14px"},model:{value:t.checked,callback:function(e){t.checked=e},expression:"checked"}},[t._v("ETH")])],1),e("div",{staticClass:"sidebar-title",staticStyle:{"margin-top":"5px"}},[t._v("Filtering Rules")]),e("div",{staticClass:"sidebar-subtitle"},[t._v("Time Interval")]),e("el-input",{staticStyle:{width:"200px"},model:{value:t.blockThreshold,callback:function(e){t.blockThreshold=e},expression:"blockThreshold"}}),e("div",{staticClass:"sidebar-subtitle"},[t._v("Value Difference")]),e("el-input",{staticStyle:{width:"200px"},model:{value:t.value,callback:function(e){t.value=e},expression:"value"}})],2),e("div",{staticStyle:{"margin-top":"20px","text-align":"center",width:"100%",position:"absolute",left:"0"}},[e("el-button",{staticStyle:{"font-size":"large"},attrs:{type:"primary"},on:{click:t.search}},[t._v("Search")])],1)]),e("div",[e("div",{staticClass:"search-content",staticStyle:{width:"1200px"}},[e("div",{staticClass:"search-area",staticStyle:{"border-top":"1px solid lightgray","border-bottom":"1px solid lightgray"}},[e("div",{staticClass:"eth-info"},[e("div",{staticClass:"eth",staticStyle:{width:"28%"}},[e("div",{staticClass:"eth-price"},[e("img",{staticClass:"info-img",attrs:{src:"/static/images/icon-8.svg"}}),e("div",{staticStyle:{"margin-left":"10%"}},[e("div",{staticClass:"info-tile"},[t._v("Monitoring Duration")]),e("div",{staticClass:"info-content",staticStyle:{"font-weight":"700",color:"gray"}},[t._v(t._s(this.dashboard.hour)+":"+t._s(this.dashboard.minute<10?"0"+this.dashboard.minute:this.dashboard.minute)+":"+t._s(this.dashboard.seconds<10?"0"+this.dashboard.seconds:this.dashboard.seconds))])])])]),t._m(1),e("div",{staticClass:"block",staticStyle:{width:"38%"}},[e("div",{staticClass:"block-latest"},[e("img",{staticClass:"info-img",staticStyle:{"margin-left":"10px"},attrs:{src:"/static/images/icon-51.svg"}}),e("div",{staticClass:"info-body"},[e("div",{staticClass:"info-tile"},[t._v("Lastest Block")]),e("div",{staticClass:"info-content",staticStyle:{"font-weight":"700",color:"skyblue"}},[t._v(t._s(this.blockNumber))])]),e("div",{staticClass:"info-body",staticStyle:{"margin-left":"10%"}},[e("div",{staticClass:"info-tile"},[t._v("Timestamp")]),e("div",{staticClass:"info-content",staticStyle:{"font-weight":"700"}},[e("span",{staticStyle:{color:"gray"}},[t._v(t._s(this.realTime))])])])])])])])]),e("el-tabs",{staticStyle:{"margin-left":"1%"},model:{value:t.activeName,callback:function(e){t.activeName=e},expression:"activeName"}},[e("el-tab-pane",{staticStyle:{width:"100%"},attrs:{label:"Overview",name:"OverviewTab"}},[e("div",{staticClass:"search-result"},[e("div",{staticClass:"search-result"},[e("div",{staticClass:"table-result"},[e("OverviewGraph",{ref:"OverviewGraph",staticStyle:{width:"100%","min-height":"800px"}})],1)])])]),e("el-tab-pane",{staticStyle:{width:"100%"},attrs:{label:"Analyze",name:"AnalyzeTab"}},[e("div",{staticClass:"search-result"},[e("div",{staticClass:"search-result"},[e("div",{staticClass:"table-result"},[e("AnalyzeGraph",{ref:"AnalyzeGraph",staticStyle:{width:"100%","min-height":"800px"}})],1)])])])],1)],1)])},s=[function(){var t=this,e=t._self._c;return e("div",{staticStyle:{height:"40px","align-items":"center"}},[e("img",{staticStyle:{width:"29px","margin-top":"5.5px"},attrs:{src:"https://raw.githubusercontent.com/Liuyushiii/img/master/USDC.png"}})])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"transaction-block",staticStyle:{width:"34%"}},[e("div",{staticClass:"transaction"},[e("img",{staticClass:"info-img",attrs:{src:"/static/images/icon-2-1.svg"}}),e("div",{staticClass:"info-body"},[e("div",{staticClass:"info-tile"},[t._v("Daily / Total Synchronized Txs")]),e("div",{staticClass:"info-content",staticStyle:{color:"orange","font-weight":"700"}},[t._v("1,011.8K / 1,860.1 M")])])])])}],o=(i(7658),function(){var t=this,e=t._self._c;return e("div",{staticStyle:{width:"100%"}},[e("div",{directives:[{name:"show",rawName:"v-show",value:!t.empty,expression:"!empty"}],staticClass:"choice"},[t._m(0),t._m(1)]),e("el-empty",{directives:[{name:"show",rawName:"v-show",value:t.empty,expression:"empty"}],staticStyle:{width:"100%"},attrs:{description:"No Data"}}),e("div",{directives:[{name:"show",rawName:"v-show",value:!t.empty,expression:"!empty"}],staticStyle:{width:"1200px",height:"800px"},attrs:{id:"analyze"}})],1)}),r=[function(){var t=this,e=t._self._c;return e("div",{staticClass:"each-choice",staticStyle:{background:"lightgray","border-bottom":"1px solid white"}},[e("img",{attrs:{src:"https://raw.githubusercontent.com/Liuyushiii/img/master/ETH.png"}}),e("span",{staticStyle:{"font-size":"small","font-weight":"700","margin-left":"10px"}},[t._v("ETH")])])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"each-choice",staticStyle:{background:"lightgray"}},[e("img",{attrs:{src:"https://raw.githubusercontent.com/Liuyushiii/img/master/USDC.png"}}),e("span",{staticStyle:{"font-size":"small","font-weight":"700","margin-left":"7.5px"}},[t._v("USDC")])])}],l={name:"AnalyzeGraph",props:["option"],data(){return{empty:!0,chart:void 0}},mounted(){},methods:{changeAnalyzeGraph:function(t){console.log(t),this.empty=!1,this.Draw(t["nodes"],t["edges"])},Draw:function(t,e){void 0!=this.chart&&this.chart.destroy(),void 0!=this.graph&&(this.graph.destroy(),this.graph=void 0),this.nodesNumber=t.length,this.edgesNumber=e.length;const i=new this.$antv.Tooltip({offsetX:10,offsetY:10,itemTypes:["node","edge"],getContent:t=>{const e=document.createElement("div");return e.style.padding="0px 40px 0px 20px","node"==t.item.getType()?e.innerHTML=`\n        <h4>Account Information</h4>\n        <ul>\n            <li>Address: ${t.item.getModel().id}</li>\n        </ul>`:"edge"==t.item.getType()&&(e.innerHTML=`\n        <h4>Transaction Information</h4>\n        <ul>\n          <li>From: ${t.item.getModel().source}</li>\n          <li>To: ${t.item.getModel().target}</li>\n          <li>Value: ${t.item.getModel().value}</li>\n        </ul>\n        `),e},shouldBegin:t=>{let e=!0;switch(t.item.getModel().id){case"1":e=!1;break;case"2":e="text-shape"===t.target.get("name");break;case"3":e="text-shape"!==t.target.get("name");break;default:e=!0;break}return e}}),a=(document.getElementById("analyze"),1200),n=800,s=30,o=["#9EC9FF","#5AC8A6","#F6C816","#E8684A","#6DC8EC","#9270CA","#FF9D4D","#269A99","#FF99C3"],r=new this.$antv.Graph({container:"analyze",width:a,height:n,layout:{type:"dagre",rankdir:"LR",align:void 0,nodesep:50,ranksep:50,controlPoints:!0},defaultNode:{type:"circle",size:s,style:{fill:"#9EC9FF",lineWidth:1,stroke:""},labelCfg:{position:"top",style:{fontSize:15,fontWeight:700}}},defaultEdge:{style:{lineWidth:1.5,endArrow:!0},labelCfg:{autoRotate:!0}},plugins:[i],modes:{default:["drag-canvas","drag-node","zoom-canvas"]}});function l(t,e){if(e>5){var i=t.substring(0,5),a=t.substring(t.length-3);return i+"..."+a}return""}function c(t){return t>=5&&t<=10?o[1]:t>10?o[2]:o[0]}t.forEach((t=>{var e=t.id,i=t.degree;t.cluster=0,t.label=l(e,i),t.style={fill:c(i)}})),r.data({nodes:t,edges:e}),r.render(),r.on("node:click",(t=>{const{item:e}=t;e.toFront()})),this.graph=r}}},c=l,d=i(1001),h=(0,d.Z)(c,o,r,!1,null,null,null),u=h.exports,p=function(){var t=this,e=t._self._c;return e("div",{staticStyle:{width:"100%"}},[e("div",{directives:[{name:"show",rawName:"v-show",value:!t.empty,expression:"!empty"}],staticClass:"diy-legend"},[e("div",{staticStyle:{width:"100%","text-align":"center","font-size":"large","font-weight":"700"}},[t._v("Statistics")]),e("div",{staticStyle:{"margin-left":"5%"}},[e("li",[t._v("Number of Nodes: "+t._s(t.nodesNumber))]),e("li",[t._v("Number of Edges: "+t._s(t.edgesNumber))])]),e("div",{attrs:{id:"pie"}})]),e("div",{directives:[{name:"show",rawName:"v-show",value:!t.empty,expression:"!empty"}],staticClass:"choice"},[t._m(0),t._m(1)]),e("el-empty",{directives:[{name:"show",rawName:"v-show",value:t.empty,expression:"empty"}],staticStyle:{width:"100%"},attrs:{description:"No Data"}}),e("div",{directives:[{name:"show",rawName:"v-show",value:!t.empty,expression:"!empty"}],staticStyle:{width:"1200px",height:"800px"},attrs:{id:"overview"}})],1)},m=[function(){var t=this,e=t._self._c;return e("div",{staticClass:"each-choice",staticStyle:{background:"lightgray"}},[e("img",{attrs:{src:"https://raw.githubusercontent.com/Liuyushiii/img/master/ETH.png"}}),e("span",{staticStyle:{"font-size":"small","font-weight":"700","margin-left":"10px"}},[t._v("ETH")])])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"each-choice"},[e("img",{attrs:{src:"https://raw.githubusercontent.com/Liuyushiii/img/master/USDC.png"}}),e("span",{staticStyle:{"font-size":"small","font-weight":"700","margin-left":"7.5px"}},[t._v("USDC")])])}],g={name:"OverviewGraph",props:["option"],data(){return{empty:!0,chart:void 0,graph:void 0,nodesNumber:0,edgesNumber:0}},mounted(){},methods:{changeOverviewGraph:function(t){console.log(t),this.empty=!1,this.Draw(t["nodes"],t["edges"]),this.pie(t["json"])},pie:function(t){var e=this.$echarts.init(document.getElementById("pie"),"white",{renderer:"canvas"});e.clear(),t={animation:!0,animationThreshold:2e3,animationDuration:1e3,animationEasing:"cubicOut",animationDelay:0,animationDurationUpdate:300,animationEasingUpdate:"cubicOut",animationDelayUpdate:0,color:["#9EC9FF","#5AC8A6","#F6C816","#E8684A","#6DC8EC","#9270CA","#FF9D4D","#269A99","#FF99C3"],series:[{type:"pie",clockwise:!0,data:t,radius:["40%","75%"],center:["50%","40%"],label:{show:!0,position:"inner",margin:8,formatter:"{b}:{c}"},rippleEffect:{show:!0,brushType:"stroke",scale:2.5,period:4}}],legend:[{data:["1-5","6-10",">10"],selected:{},show:!0,orient:"horizontal",x:"center",y:"bottom",itemGap:10,itemWidth:20,itemHeight:14}],tooltip:{show:!0,trigger:"item",triggerOn:"mousemove|click",axisPointer:{type:"line"},showContent:!0,alwaysShowContent:!1,showDelay:0,hideDelay:100,textStyle:{fontSize:14},borderWidth:0,padding:5}},e.setOption(t)},Draw:function(t,e){void 0!=this.chart&&this.chart.destroy(),void 0!=this.graph&&(this.graph.destroy(),this.graph=void 0),this.nodesNumber=t.length,this.edgesNumber=e.length;const i=new this.$antv.Tooltip({offsetX:10,offsetY:10,itemTypes:["node","edge"],getContent:t=>{const e=document.createElement("div");return e.style.padding="0px 40px 0px 20px","node"==t.item.getType()?e.innerHTML=`\n        <h4>Account Information</h4>\n        <ul>\n            <li>Address: ${t.item.getModel().id}</li>\n        </ul>`:"edge"==t.item.getType()&&(e.innerHTML=`\n        <h4>Transaction Information</h4>\n        <ul>\n          <li>From: ${t.item.getModel().source}</li>\n          <li>To: ${t.item.getModel().target}</li>\n          <li>Value: ${t.item.getModel().value}</li>\n        </ul>\n        `),e},shouldBegin:t=>{let e=!0;switch(t.item.getModel().id){case"1":e=!1;break;case"2":e="text-shape"===t.target.get("name");break;case"3":e="text-shape"!==t.target.get("name");break;default:e=!0;break}return e}}),a=(document.getElementById("overview"),1200),n=800,s=10,o=["#9EC9FF","#5AC8A6","#F6C816","#E8684A","#6DC8EC","#9270CA","#FF9D4D","#269A99","#FF99C3"],r=new this.$antv.Graph({container:"overview",width:a,height:n,layout:{type:"force",preventOverlap:!0,nodeSpacing:15,clustering:!1},defaultNode:{type:"circle",size:s,style:{fill:"#9EC9FF",lineWidth:1,stroke:""},labelCfg:{position:"top",style:{fontSize:15,fontWeight:700}}},defaultEdge:{style:{lineWidth:1.5,endArrow:!0},labelCfg:{autoRotate:!0}},plugins:[i],modes:{default:["drag-canvas","drag-node","zoom-canvas"]}});function l(t,e){if(e>5){var i=t.substring(0,5),a=t.substring(t.length-3);return i+"..."+a}return""}function c(t){return t>=5&&t<=10?o[1]:t>10?o[2]:o[0]}t.forEach((t=>{var e=t.id,i=t.degree;t.cluster=0,t.label=l(e,i),t.style={fill:c(i)}})),r.data({nodes:t,edges:e}),r.render(),r.on("node:click",(t=>{const{item:e}=t;e.toFront()})),this.graph=r}}},v=g,f=(0,d.Z)(v,p,m,!1,null,null,null),y=f.exports,b={name:"App",components:{AnalyzeGraph:u,OverviewGraph:y},data(){return{activeIndex:"1",activeName:"OverviewTab",option4Overview:{},option4Analyze:{},tableData:[],MaxBlocknumber:15365903,checked:!0,value1:!0,MinBlocknumber:15265903,jump:0,token:"Eth",blockThreshold:7200,value:5,realTime:(new Date).toLocaleString(),accounts:["0xc611952d81e4ecbd17c8f963123dec5d7bce1c274"],contracts:["0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"],blockNumber:16540597,txTimer:void 0,blockTime:"Unknown",dashboard:{hour:0,minute:0,seconds:0}}},created(){setInterval((()=>{let t=new Date;this.realTime=t.toLocaleString();let e="2022/6/23 0:00:00",i=t.getTime()-new Date(e).getTime();this.dashboard.hour=parseInt(i/36e5),this.dashboard.minute=parseInt(i%36e5/6e4),this.dashboard.seconds=parseInt(i%6e4/1e3)}),1e3)},mounted(){},methods:{getInputStyle:function(){return this.accounts.length>1?"width: 170px; margin-right: 10px":"width: 200px"},getcontractsInputStyle:function(){return this.contracts.length>1?"width: 110px; margin-left: 10px;margin-right: 10px":"width: 160px; margin-left: 10px"},addContract:function(t){this.contracts.push("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")},deleteContract:function(t,e){this.contracts.length<=1||this.contracts.splice(e,1)},addAccount:function(t){this.accounts.push("0xc611952d81e4ecbd17c8f963123dec5d7bce1c274")},deleteAccount:function(t,e){this.accounts.length<=1||this.accounts.splice(e,1)},changeChart:function(){this.$refs.AnalyzeGraph.changeAnalyzeGraph(this.option4Analyze),this.$refs.OverviewGraph.changeOverviewGraph(this.option4Overview)},search:function(){this.$http.post("/data/analyze/",{type:"query",address:this.accounts,khop:this.jump,start_blk:this.MinBlocknumber,end_blk:this.MaxBlocknumber,contracts:this.contracts,timeInterval:this.blockThreshold,valueDifference:this.value},{headers:{"Content-Type":"application/json"}},{emulateJSON:!0}).then((function(t){this.code=200,this.option4Analyze={nodes:t.body.analyze.nodes,edges:t.body.analyze.edges},this.$refs.AnalyzeGraph.changeAnalyzeGraph(this.option4Analyze),this.option4Overview={nodes:t.body.overview.nodes,edges:t.body.overview.edges,json:t.body.overview.json},this.$refs.OverviewGraph.changeOverviewGraph(this.option4Overview)}),(function(t){this.code=t.status,this.message=t.body.message}))}}},w=b,x=(0,d.Z)(w,n,s,!1,null,null,null),C=x.exports,S=i(2631);a["default"].use(S.Z);var k=new S.Z({mode:"history",routes:[{path:"/",name:"index"}]}),_=i(9618),T=i(3845),A=i(8499),z=i.n(A),D=i(7752),E=i(6642);a["default"].use(E.ZP),a["default"].use(z()),a["default"].config.productionTip=!1,a["default"].prototype.zrender=_,a["default"].prototype.$echarts=T,a["default"].prototype.$antv=D.ZP,new a["default"]({render:t=>t(C),router:k}).$mount("#app")},6608:function(){}},e={};function i(a){var n=e[a];if(void 0!==n)return n.exports;var s=e[a]={id:a,loaded:!1,exports:{}};return t[a].call(s.exports,s,s.exports,i),s.loaded=!0,s.exports}i.m=t,function(){var t=[];i.O=function(e,a,n,s){if(!a){var o=1/0;for(d=0;d<t.length;d++){a=t[d][0],n=t[d][1],s=t[d][2];for(var r=!0,l=0;l<a.length;l++)(!1&s||o>=s)&&Object.keys(i.O).every((function(t){return i.O[t](a[l])}))?a.splice(l--,1):(r=!1,s<o&&(o=s));if(r){t.splice(d--,1);var c=n();void 0!==c&&(e=c)}}return e}s=s||0;for(var d=t.length;d>0&&t[d-1][2]>s;d--)t[d]=t[d-1];t[d]=[a,n,s]}}(),function(){i.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return i.d(e,{a:e}),e}}(),function(){i.d=function(t,e){for(var a in e)i.o(e,a)&&!i.o(t,a)&&Object.defineProperty(t,a,{enumerable:!0,get:e[a]})}}(),function(){i.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(t){if("object"===typeof window)return window}}()}(),function(){i.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)}}(),function(){i.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})}}(),function(){i.nmd=function(t){return t.paths=[],t.children||(t.children=[]),t}}(),function(){var t={143:0};i.O.j=function(e){return 0===t[e]};var e=function(e,a){var n,s,o=a[0],r=a[1],l=a[2],c=0;if(o.some((function(e){return 0!==t[e]}))){for(n in r)i.o(r,n)&&(i.m[n]=r[n]);if(l)var d=l(i)}for(e&&e(a);c<o.length;c++)s=o[c],i.o(t,s)&&t[s]&&t[s][0](),t[s]=0;return i.O(d)},a=self["webpackChunkdemo4sraft"]=self["webpackChunkdemo4sraft"]||[];a.forEach(e.bind(null,0)),a.push=e.bind(null,a.push.bind(a))}();var a=i.O(void 0,[998],(function(){return i(7186)}));a=i.O(a)})();
//# sourceMappingURL=app.bb3a9d2b.js.map
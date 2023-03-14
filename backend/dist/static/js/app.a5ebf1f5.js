(function(){var t={7462:function(t,e,i){"use strict";var n=i(6369),a=function(){var t=this,e=t._self._c;return e("div",{staticStyle:{width:"100%",display:"flex","margin-top":"20px","margin-left":"100px","border-bottom":"1px solid lightgray","border-right":"1px solid lightgray"},attrs:{id:"app"}},[e("div",{staticClass:"sidebar",staticStyle:{width:"250px",position:"relative"}},[e("div",{staticStyle:{width:"100%","font-size":"x-large","font-weight":"700","text-align":"center"}},[t._v("GraphSword")]),e("div",{staticClass:"sidebar-form"},[e("div",{staticClass:"sidebar-title"},[t._v("Address")]),t._l(t.accounts,(function(i,n){return e("div",{key:n,staticStyle:{display:"flex","margin-top":"5px"}},[e("div",[e("el-input",{style:t.getInputStyle(),model:{value:t.accounts[n],callback:function(e){t.$set(t.accounts,n,e)},expression:"accounts[index]"}})],1),e("div",{staticStyle:{height:"40px","line-height":"40px","align-items":"center"}},[e("el-button",{directives:[{name:"show",rawName:"v-show",value:t.accounts.length>1,expression:"accounts.length > 1"}],attrs:{type:"danger",icon:"el-icon-delete",circle:"",size:"mini"},on:{click:function(e){return t.deleteAccount(e,n)}}})],1)])})),e("div",{staticStyle:{"margin-top":"5px","text-align":"center",width:"100%",position:"absolute",left:"0"}},[e("el-button",{attrs:{icon:"el-icon-plus",circle:"",size:"mini"},on:{click:function(e){return t.addAccount(e)}}})],1),e("div",{staticClass:"sidebar-title",staticStyle:{"margin-top":"25px"}},[t._v("K-hop Steps")]),e("el-input",{staticStyle:{width:"200px"},model:{value:t.jump,callback:function(e){t.jump=e},expression:"jump"}}),e("div",{staticClass:"sidebar-title"},[t._v("Query Window(by block)")]),e("div",{staticStyle:{display:"flex","margin-top":"20px"}},[e("div",{staticClass:"sidebar-subtitle"},[t._v("Start_blk:")]),e("el-input",{staticStyle:{width:"130px"},model:{value:t.MinBlocknumber,callback:function(e){t.MinBlocknumber=e},expression:"MinBlocknumber"}})],1),e("div",{staticStyle:{display:"flex","margin-top":"20px"}},[e("div",{staticClass:"sidebar-subtitle"},[t._v("End_blk:")]),e("el-input",{staticStyle:{width:"130px","margin-left":"7px"},model:{value:t.MaxBlocknumber,callback:function(e){t.MaxBlocknumber=e},expression:"MaxBlocknumber"}})],1),e("div",{staticClass:"sidebar-title"},[t._v("Contract Address")]),t._l(t.contracts,(function(i,n){return e("div",{key:n,staticStyle:{display:"flex","margin-top":"5px"}},[t._m(0,!0),e("div",[e("el-input",{style:t.getcontractsInputStyle(),model:{value:t.contracts[n],callback:function(e){t.$set(t.contracts,n,e)},expression:"contracts[index]"}})],1),e("div",{staticStyle:{height:"40px","line-height":"40px","align-items":"center"}},[e("el-button",{directives:[{name:"show",rawName:"v-show",value:t.contracts.length>1,expression:"contracts.length > 1"}],attrs:{type:"danger",icon:"el-icon-delete",circle:"",size:"mini"},on:{click:function(e){return t.deleteContract(e,n)}}})],1)])})),e("div",{staticStyle:{"margin-top":"5px","text-align":"center",width:"100%",position:"absolute",left:"0"}},[e("el-button",{attrs:{icon:"el-icon-plus",circle:"",size:"mini"},on:{click:function(e){return t.addContract(e)}}})],1),e("div",{staticClass:"sidebar-title",staticStyle:{"margin-top":"40px"}},[t._v("Filter Rules")]),e("div",{staticClass:"sidebar-subtitle"},[t._v("Time Interval(by block)")]),e("el-input",{staticStyle:{width:"200px"},model:{value:t.blockThreshold,callback:function(e){t.blockThreshold=e},expression:"blockThreshold"}}),e("div",{staticClass:"sidebar-subtitle"},[t._v("Value Difference")]),e("el-input",{staticStyle:{width:"200px"},model:{value:t.value,callback:function(e){t.value=e},expression:"value"}})],2),e("div",{staticStyle:{"margin-top":"20px","text-align":"center",width:"100%",position:"absolute",left:"0"}},[e("el-button",{attrs:{type:"primary"},on:{click:t.search}},[t._v("Search")])],1),t._m(1)]),e("div",[e("div",{staticClass:"search-content",staticStyle:{width:"1200px"}},[e("div",{staticClass:"search-area",staticStyle:{"border-top":"1px solid lightgray","border-bottom":"1px solid lightgray"}},[e("div",{staticClass:"eth-info"},[e("div",{staticClass:"eth",staticStyle:{width:"25%"}},[e("div",{staticClass:"eth-price"},[e("img",{staticClass:"info-img",attrs:{src:"/static/images/icon-8.svg"}}),e("div",{staticStyle:{"margin-left":"10%"}},[e("div",{staticClass:"info-tile"},[t._v("Monitoring Duration")]),e("div",{staticClass:"info-content",staticStyle:{"font-weight":"700"}},[t._v(t._s(this.dashboard.hour)+":"+t._s(this.dashboard.minute<10?"0"+this.dashboard.minute:this.dashboard.minute)+":"+t._s(this.dashboard.seconds<10?"0"+this.dashboard.seconds:this.dashboard.seconds))])])])]),t._m(2),e("div",{staticClass:"block",staticStyle:{width:"35%"}},[e("div",{staticClass:"block-latest"},[e("img",{staticClass:"info-img",staticStyle:{"margin-left":"10px"},attrs:{src:"/static/images/icon-51.svg"}}),e("div",{staticClass:"info-body"},[e("div",{staticClass:"info-tile"},[t._v("Lastest Block")]),e("div",{staticClass:"info-content",staticStyle:{"font-weight":"700",color:"skyblue"}},[t._v(t._s(this.blockNumber))])]),t._m(3)])])])])]),e("el-tabs",{staticStyle:{"margin-left":"1%"},model:{value:t.activeName,callback:function(e){t.activeName=e},expression:"activeName"}},[e("el-tab-pane",{staticStyle:{width:"100%"},attrs:{label:"Overview",name:"OverviewTab"}},[e("div",{staticClass:"search-result"},[e("div",{staticClass:"search-result"},[e("div",{staticClass:"table-result"},[e("OverviewGraph",{staticStyle:{width:"100%","min-height":"800px"},attrs:{option:t.option4Overview}})],1)])])]),e("el-tab-pane",{staticStyle:{width:"100%"},attrs:{label:"Analyze",name:"AnalyzeTab"}},[e("div",{staticClass:"search-result"},[e("div",{staticClass:"search-result"},[e("div",{staticClass:"table-result"},[e("AnalyzeGraph",{staticStyle:{width:"100%","min-height":"800px"},attrs:{option:t.option4Analyze}})],1)])])])],1)],1)])},s=[function(){var t=this,e=t._self._c;return e("div",{staticStyle:{height:"40px","align-items":"center"}},[e("img",{staticStyle:{width:"29px","margin-top":"5.5px"},attrs:{src:"https://raw.githubusercontent.com/Liuyushiii/img/master/USDC.png"}})])},function(){var t=this,e=t._self._c;return e("div",{staticStyle:{position:"absolute","margin-top":"160px",width:"100%",left:"0"}},[e("img",{staticStyle:{width:"100px","margin-left":"13px"},attrs:{src:"https://raw.githubusercontent.com/Liuyushiii/img/master/ecnu.png"}}),e("img",{staticStyle:{width:"100px"},attrs:{src:"https://raw.githubusercontent.com/Liuyushiii/img/master/antchain.png"}})])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"transaction-block",staticStyle:{width:"40%"}},[e("div",{staticClass:"transaction"},[e("img",{staticClass:"info-img",attrs:{src:"/static/images/icon-2-1.svg"}}),e("div",{staticClass:"info-body"},[e("div",{staticClass:"info-tile"},[t._v("Synchronized Txs")]),e("div",{staticClass:"info-content",staticStyle:{color:"orange","font-weight":"700"}},[t._v("1860.1M")])]),e("div",{staticClass:"info-body"},[e("div",{staticClass:"info-tile"},[t._v("Daily Synchronized Txs")]),e("div",{staticClass:"info-content",staticStyle:{color:"yellowgreen","font-weight":"700"}},[t._v("1,011,772")])])])])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"info-body",staticStyle:{"margin-left":"10%"}},[e("div",{staticClass:"info-tile"},[t._v("Timestamp")]),e("div",{staticClass:"info-content",staticStyle:{"font-weight":"700"}},[e("span",{staticStyle:{color:"gray"}},[t._v("2023/3/7 13:16:46")])])])}],o=(i(7658),function(){var t=this,e=t._self._c;return e("div",{staticStyle:{width:"100%"}},[e("div",{directives:[{name:"show",rawName:"v-show",value:!t.empty,expression:"!empty"}],staticClass:"choice"},[t._m(0),t._m(1)]),e("el-empty",{directives:[{name:"show",rawName:"v-show",value:t.empty,expression:"empty"}],staticStyle:{width:"100%"},attrs:{description:"No Data"}}),e("div",{directives:[{name:"show",rawName:"v-show",value:!t.empty,expression:"!empty"}],staticStyle:{width:"1200px",height:"800px"},attrs:{id:"analyze"}})],1)}),l=[function(){var t=this,e=t._self._c;return e("div",{staticClass:"each-choice",staticStyle:{background:"lightgray","border-bottom":"1px solid white"}},[e("img",{attrs:{src:"https://raw.githubusercontent.com/Liuyushiii/img/master/ETH.png"}}),e("span",{staticStyle:{"font-size":"small","font-weight":"700","margin-left":"10px"}},[t._v("ETH")])])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"each-choice",staticStyle:{background:"lightgray"}},[e("img",{attrs:{src:"https://raw.githubusercontent.com/Liuyushiii/img/master/USDC.png"}}),e("span",{staticStyle:{"font-size":"small","font-weight":"700","margin-left":"7.5px"}},[t._v("USDC")])])}],r={name:"AnalyzeGraph",props:["option"],data(){return{empty:!0,chart:void 0}},mounted(){},watch:{option(t){console.log(t),this.empty=!1,this.Draw(t["nodes"],t["edges"],t["dic"])}},methods:{Draw:function(t,e){void 0!=this.chart&&this.chart.destroy();const i=new this.$antv.Tooltip({offsetX:10,offsetY:10,itemTypes:["node","edge"],getContent:t=>{const e=document.createElement("div");return e.style.padding="0px 40px 0px 20px","node"==t.item.getType()?e.innerHTML=`\n        <h4>Account Information</h4>\n        <ul>\n            <li>Address: ${t.item.getModel().id}</li>\n            <li>x: ${t.item.getModel().x}</li>\n            <li>y: ${t.item.getModel().y}</li>\n        </ul>`:"edge"==t.item.getType()&&(e.innerHTML=`\n        <h4>Transaction Information</h4>\n        <ul>\n          <li>From: ${t.item.getModel().source}</li>\n          <li>To: ${t.item.getModel().target}</li>\n          <li>Value: ${t.item.getModel().value}</li>\n        </ul>\n        `),e},shouldBegin:t=>{let e=!0;switch(t.item.getModel().id){case"1":e=!1;break;case"2":e="text-shape"===t.target.get("name");break;case"3":e="text-shape"!==t.target.get("name");break;default:e=!0;break}return e}}),n=(document.getElementById("analyze"),1200),a=800,s=10,o=(new this.$antv.Grid,new this.$antv.Graph({container:"analyze",width:n,height:a,defaultNode:{type:"circle",size:s,style:{fill:"#DA5914",lineWidth:0},labelCfg:{position:"right"}},defaultEdge:{style:{endArrow:{path:this.$antv.Arrow.vee(7,8,5),d:0,fill:"black",arrowPosition:.5},lineWidth:1,stroke:"#778899"},labelCfg:{autoRotate:!0}},plugins:[i],modes:{default:["drag-canvas","drag-node","zoom-canvas"]}}));t.forEach((t=>{"null"==t.label&&(t.label="")})),o.data({nodes:t,edges:e}),o.render(),o.on("node:dragend",(t=>{console.log(t.item.getModel().id+","+t.x+","+t.y)}))}}},c=r,d=i(1001),u=(0,d.Z)(c,o,l,!1,null,null,null),h=u.exports,p=function(){var t=this,e=t._self._c;return e("div",{staticStyle:{width:"100%"}},[e("div",{directives:[{name:"show",rawName:"v-show",value:!t.empty,expression:"!empty"}],staticClass:"diy-legend"},[e("div",{staticStyle:{width:"100%","text-align":"center","font-size":"large","font-weight":"700"}},[t._v("Statistics")]),e("li",[t._v("Number of Nodes:"+t._s(t.nodesNumber))]),e("li",[t._v("Number of Edges:"+t._s(t.edgesNumber))]),e("div",{attrs:{id:"pie"}})]),e("div",{directives:[{name:"show",rawName:"v-show",value:!t.empty,expression:"!empty"}],staticClass:"choice"},[t._m(0),t._m(1)]),e("el-empty",{directives:[{name:"show",rawName:"v-show",value:t.empty,expression:"empty"}],staticStyle:{width:"100%"},attrs:{description:"No Data"}}),e("div",{directives:[{name:"show",rawName:"v-show",value:!t.empty,expression:"!empty"}],staticStyle:{width:"1200px",height:"800px"},attrs:{id:"overview"}})],1)},m=[function(){var t=this,e=t._self._c;return e("div",{staticClass:"each-choice",staticStyle:{background:"lightgray"}},[e("img",{attrs:{src:"https://raw.githubusercontent.com/Liuyushiii/img/master/ETH.png"}}),e("span",{staticStyle:{"font-size":"small","font-weight":"700","margin-left":"10px"}},[t._v("ETH")])])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"each-choice"},[e("img",{attrs:{src:"https://raw.githubusercontent.com/Liuyushiii/img/master/USDC.png"}}),e("span",{staticStyle:{"font-size":"small","font-weight":"700","margin-left":"7.5px"}},[t._v("USDC")])])}],g={name:"OverviewGraph",props:["option"],data(){return{empty:!0,chart:void 0,nodesNumber:0,edgesNumber:0}},mounted(){},watch:{option(t){this.empty=!1,this.Draw(t["nodes"],t["edges"]),this.pie(t["json"])}},methods:{pie:function(t){var e=this.$echarts.init(document.getElementById("pie"),"white",{renderer:"canvas"});e.clear(),t={animation:!0,animationThreshold:2e3,animationDuration:1e3,animationEasing:"cubicOut",animationDelay:0,animationDurationUpdate:300,animationEasingUpdate:"cubicOut",animationDelayUpdate:0,color:["#9EC9FF","#5AC8A6","#F6C816","#E8684A","#6DC8EC","#9270CA","#FF9D4D","#269A99","#FF99C3"],series:[{type:"pie",clockwise:!0,data:t,radius:["40%","75%"],center:["50%","50%"],label:{show:!0,position:"inner",margin:8,formatter:"{b}:{c}"},rippleEffect:{show:!0,brushType:"stroke",scale:2.5,period:4}}],legend:[{data:["1-5","6-10",">10"],selected:{},show:!0,left:"0%",bottom:"0%",itemGap:10,itemWidth:20,itemHeight:14}],tooltip:{show:!0,trigger:"item",triggerOn:"mousemove|click",axisPointer:{type:"line"},showContent:!0,alwaysShowContent:!1,showDelay:0,hideDelay:100,textStyle:{fontSize:14},borderWidth:0,padding:5}},e.setOption(t)},Draw:function(t,e){void 0!=this.chart&&this.chart.destroy(),this.nodesNumber=t.length,this.edgesNumber=e.length;const i=new this.$antv.Tooltip({offsetX:10,offsetY:10,itemTypes:["node","edge"],getContent:t=>{const e=document.createElement("div");return e.style.padding="0px 40px 0px 20px","node"==t.item.getType()?e.innerHTML=`\n        <h4>Account Information</h4>\n        <ul>\n            <li>Address: ${t.item.getModel().id}</li>\n        </ul>`:"edge"==t.item.getType()&&(e.innerHTML=`\n        <h4>Transaction Information</h4>\n        <ul>\n          <li>From: ${t.item.getModel().source}</li>\n          <li>To: ${t.item.getModel().target}</li>\n          <li>Value: ${t.item.getModel().value}</li>\n        </ul>\n        `),e},shouldBegin:t=>{let e=!0;switch(t.item.getModel().id){case"1":e=!1;break;case"2":e="text-shape"===t.target.get("name");break;case"3":e="text-shape"!==t.target.get("name");break;default:e=!0;break}return e}}),n=(document.getElementById("overview"),1200),a=800,s=10,o=["#9EC9FF","#5AC8A6","#F6C816","#E8684A","#6DC8EC","#9270CA","#FF9D4D","#269A99","#FF99C3"],l=new this.$antv.Graph({container:"overview",width:n,height:a,layout:{nodeSpacing:15,clustering:"false"},defaultNode:{type:"circle",size:s,style:{fill:"#9EC9FF",lineWidth:1,stroke:""},labelCfg:{position:"top",style:{fontSize:15,fontWeight:700}}},defaultEdge:{style:{lineWidth:1.5,endArrow:!0},labelCfg:{autoRotate:!0}},plugins:[i],modes:{default:["drag-canvas","drag-node","zoom-canvas"]}});function r(t,e){if(e>5){var i=t.substring(0,5),n=t.substring(t.length-3);return i+"..."+n}return""}function c(t){return t>=5&&t<=10?o[1]:t>10?o[2]:o[0]}t.forEach((t=>{var e=t.id,i=t.degree;t.cluster=0,t.label=r(e,i),t.style={fill:c(i)}})),l.data({nodes:t,edges:e}),l.render(),l.on("node:click",(t=>{const{item:e}=t;e.toFront()}))}}},v=g,f=(0,d.Z)(v,p,m,!1,null,null,null),y=f.exports,b={name:"App",components:{AnalyzeGraph:h,OverviewGraph:y},data(){return{activeIndex:"1",activeName:"OverviewTab",option4Overview:{},option4Analyze:{},tableData:[],MaxBlocknumber:15365903,value1:!0,MinBlocknumber:15265903,jump:0,token:"Eth",blockThreshold:7200,value:5,accounts:["0xc611952d81e4ecbd17c8f963123dec5d7bce1c274"],contracts:["0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"],blockNumber:16540597,txTimer:void 0,blockTime:"Unknown",dashboard:{hour:734,minute:46,seconds:1}}},created(){},mounted(){},methods:{getInputStyle:function(){return this.accounts.length>1?"width: 170px; margin-right: 10px":"width: 200px"},getcontractsInputStyle:function(){return this.contracts.length>1?"width: 130px; margin-left: 10px;margin-right: 10px":"width: 180px; margin-left: 10px"},addContract:function(t){this.contracts.push("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")},deleteContract:function(t,e){this.contracts.length<=1||this.contracts.splice(e,1)},addAccount:function(t){this.accounts.push("0xc611952d81e4ecbd17c8f963123dec5d7bce1c274")},deleteAccount:function(t,e){this.accounts.length<=1||this.accounts.splice(e,1)},search:function(){this.$http.post("/data/analyze/",{account:"0xi8l4rv7k4y9buf72i0lh6yw1y12aq8mwduanw940",jump:3},{headers:{"Content-Type":"application/json"}},{emulateJSON:!0}).then((function(t){this.code=200,this.option4Analyze={nodes:t.body.nodes,edges:t.body.edges}}),(function(t){this.code=t.status,this.message=t.body.message})),this.$http.post("/data/overview/",{account:"0xi8l4rv7k4y9buf72i0lh6yw1y12aq8mwduanw940",jump:3},{headers:{"Content-Type":"application/json"}},{emulateJSON:!0}).then((function(t){this.code=200,this.option4Overview={nodes:t.body.nodes,edges:t.body.edges,json:t.body.json}}),(function(t){this.code=t.status,this.message=t.body.message}))}}},w=b,x=(0,d.Z)(w,a,s,!1,null,null,null),C=x.exports,S=i(2631);n["default"].use(S.Z);var _=new S.Z({mode:"history",routes:[{path:"/",name:"index"}]}),k=i(9618),T=i(3845),A=i(8499),z=i.n(A),E=i(7752),D=i(6642);n["default"].use(D.ZP),n["default"].use(z()),n["default"].config.productionTip=!1,n["default"].prototype.zrender=k,n["default"].prototype.$echarts=T,n["default"].prototype.$antv=E.ZP,new n["default"]({render:t=>t(C),router:_}).$mount("#app")},6608:function(){}},e={};function i(n){var a=e[n];if(void 0!==a)return a.exports;var s=e[n]={id:n,loaded:!1,exports:{}};return t[n].call(s.exports,s,s.exports,i),s.loaded=!0,s.exports}i.m=t,function(){var t=[];i.O=function(e,n,a,s){if(!n){var o=1/0;for(d=0;d<t.length;d++){n=t[d][0],a=t[d][1],s=t[d][2];for(var l=!0,r=0;r<n.length;r++)(!1&s||o>=s)&&Object.keys(i.O).every((function(t){return i.O[t](n[r])}))?n.splice(r--,1):(l=!1,s<o&&(o=s));if(l){t.splice(d--,1);var c=a();void 0!==c&&(e=c)}}return e}s=s||0;for(var d=t.length;d>0&&t[d-1][2]>s;d--)t[d]=t[d-1];t[d]=[n,a,s]}}(),function(){i.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return i.d(e,{a:e}),e}}(),function(){i.d=function(t,e){for(var n in e)i.o(e,n)&&!i.o(t,n)&&Object.defineProperty(t,n,{enumerable:!0,get:e[n]})}}(),function(){i.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(t){if("object"===typeof window)return window}}()}(),function(){i.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)}}(),function(){i.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})}}(),function(){i.nmd=function(t){return t.paths=[],t.children||(t.children=[]),t}}(),function(){var t={143:0};i.O.j=function(e){return 0===t[e]};var e=function(e,n){var a,s,o=n[0],l=n[1],r=n[2],c=0;if(o.some((function(e){return 0!==t[e]}))){for(a in l)i.o(l,a)&&(i.m[a]=l[a]);if(r)var d=r(i)}for(e&&e(n);c<o.length;c++)s=o[c],i.o(t,s)&&t[s]&&t[s][0](),t[s]=0;return i.O(d)},n=self["webpackChunkdemo4sraft"]=self["webpackChunkdemo4sraft"]||[];n.forEach(e.bind(null,0)),n.push=e.bind(null,n.push.bind(n))}();var n=i.O(void 0,[998],(function(){return i(7462)}));n=i.O(n)})();
//# sourceMappingURL=app.a5ebf1f5.js.map
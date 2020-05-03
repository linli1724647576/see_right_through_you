from pyecharts import options as opts
from pyecharts.charts import Map,Map3D
from pyecharts.faker import Faker

from pyecharts.globals import ChartType
from pyecharts.commons.utils import JsCode


class Draw_map():
    def to_map_china(self,area,variate,update_time):
        pieces = [
            {'max':99999999,'min':1001,'label':'>10000','color':'#8A0808'},
            {'max': 9999, 'min': 100, 'label': '1000-9999', 'color': '#B40404'},
            {'max': 999, 'min': 100, 'label': '100-999', 'color': '#DF0101'},
            {'max': 99, 'min': 10, 'label': '10-99', 'color': '#F5A9A9'},
            {'max': 9, 'min': 1, 'label': '1-9', 'color': '#F5A9A9'},
            {'max': 0, 'min': 0, 'label': '0', 'color': '#FFFFFF'},
        ]

        c = (
            Map(init_opts=opts.InitOpts(width='1000px',height='800px'))
                .add("累计确诊人数", [list(z) for z in zip(area, variate)], "china")
                .set_global_opts(
                title_opts=opts.TitleOpts(title="中国疫情地图分布",subtitle="截止%s 中国疫情分布情况"%(update_time),
                                          pos_left='center',pos_top='30px'),
                visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True,pieces=pieces),
            )
                .render("中国疫情地图.html")
        )
    def to_map_3D_china(self,data,update_time):
        c = (
            Map3D(init_opts=opts.InitOpts(width='1200px',height='800px'))
            .add_schema(
                itemstyle_opts=opts.ItemStyleOpts(
                    color="rgb(5,101,123)",
                    opacity=1,
                    border_width=0.8,
                    border_color="rgb(62,215,213)",
                ),
                map3d_label=opts.Map3DLabelOpts(
                    is_show=False,
                    formatter=JsCode("function(data){return data.name + " " + data.value[2];}"),
                ),
                emphasis_label_opts=opts.LabelOpts(
                    is_show=False,
                    color="#fff",
                    font_size=10,
                    background_color="rgba(0,23,11,0)",
                ),
                light_opts=opts.Map3DLightOpts(
                    main_color="#fff",
                    main_intensity=1.2,
                    main_shadow_quality="high",
                    is_main_shadow=False,
                    main_beta=10,
                    ambient_intensity=0.3,
                ),
            )
            .add(
                series_name="中国3D疫情图",
                data_pair=list(zip(list(data.keys()), list(data.values()))),
                type_=ChartType.SCATTER3D,
                bar_size=1,
                shading="lambert",
                label_opts=opts.LabelOpts(
                    is_show=True,
                    formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
                ),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="中国疫情3D地图分布", subtitle="截止%s 中国疫情分布情况" % (update_time),
                                          pos_left='center', pos_top='30px')
            )
            .render("map3d_中国疫情地图.html")
        )


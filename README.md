# Pymxs
Here is some useful pymxs class ready to be use.
 ● 增加修改器的脚本
rt.addmodifier(Lp,rt.bend())
 ● 另一个选择方法：
obj=rt.selection[0]
  ● 去除模型材质：
for i in rt.selcection:
i.material = None
  ● 执行max窗口命令：
rt.execute('max command')
  ● 构造函数的方法
c = rt.box(prefix = "rabbit",height = 30)
  ● 自定义用户数据
for i in rt.selection:
	rt.setUserProp(i,"huxiede",23)
  ● lookat控制器和重置
a.target =b
a.controller = rt.prs()

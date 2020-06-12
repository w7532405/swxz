// pages/have/have.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    sex:"",
    sex_value:"",
    password1:"",
    password2:"",
    name:"",
    telephone:"",
    id_card:"",
    array:["女", "男"],
    is_select:false

  },
  getpassword1(e){
    // console.log(e.detail.value.length)
      this.setData({
        password1:e.detail.value
      })
  },
  getpassword2(e){
      this.setData({
        password2:e.detail.value
      })
  },
  bindPickerChange(e){
    // console.log(e.detail.value)
    this.setData({
      sex:e.detail.value
    })
    if(e.detail.value == 0){
      this.setData({
        sex_value:"女",
        is_select:true
      })
    }
    else{
      this.setData({
        sex_value:"男",
        is_select:true
      })
    }
  },
  getname(e){
    this.setData({
      name:e.detail.value
    })
  },
  gettelephone(e){
    this.setData({
      telephone:e.detail.value
    })
  },
  getidcard(e){
    this.setData({
      id_card:e.detail.value
    })
  },
  submit(){
    var that = this
    if ((that.data.telephone.length)>=11){
      if ((that.data.id_card.length)>=18){
        if((that.data.password1.length)>=6 && (that.data.password2.length)>=6){
          if (that.data.password1 == that.data.password2){
            wx.request({
              url: 'https://www.skylineacg.xyz/api/regist/',
              method:'POST',
              data:{
                name:that.data.name,
                telephone:that.data.telephone,
                id_card:that.data.id_card,
                sex:that.data.sex,
                password:that.data.password1,
                open_id:app.globalData.appid
              },
              success(res){
                if (res.data.status == true){
                  if(res.data.regist_re == "success"){
                    // console.log("成功")
                    wx.switchTab({
                      url: '../my/my',
                    })
                    
                  }
                  else{
                    wx.showToast({ //这里提示失败原因
                      title: '该手机号已被注册',
                      icon: 'none',
                      duration: 1000
                     })
                  }
                }
                else{
                  wx.showToast({ //这里提示失败原因
                    title: '服务器连接错误！',
                    icon: 'none',
                    duration: 1000
                   })
                }
              },
              fail(){
                wx.showToast({ //这里提示失败原因
                  title: '服务器连接错误！',
                  icon: 'none',
                  duration: 1000
                 })
              }
            })
          }
          else{
            wx.showToast({ //这里提示失败原因
              title: '俩次密码输入的密码不一致',
              icon: 'none',
              duration: 1000
             })
          }
        }
        else{
          wx.showToast({ //这里提示失败原因
            title: '密码长度不够',
            icon: 'none',
            duration: 1000
           })
        }
      }
      else{
        wx.showToast({ //这里提示失败原因
          title: '身份证长度不够',
          icon: 'none',
          duration: 1000
         })
      }
    }
    else{
      wx.showToast({ //这里提示失败原因
        title: '电话号长度不够',
        icon: 'none',
        duration: 1000
       })
    }
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(app.globalData.appid)
  },
 

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})
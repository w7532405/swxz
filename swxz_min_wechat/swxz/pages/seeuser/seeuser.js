// pages/seeuser/seeuser.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    realname:"",
    telephone1:"",
    telephone:"",
    sex:"",
    ic_card:"",
    is_active:""
  },
  change(){
    var that = this
    wx.request({
      url: 'https://www.skylineacg.xyz/api/su_show/',
      method:'POST',
      data:{
        telephone:this.data.telephone
      },
      success(res){
        console.log(res.data)
        if (res.data.is_null == "1"){
          wx.showToast({
            title: '查无此人',
          })
        }
        if (res.data.status == true){
          // console.log(res.data.detail)
          app.User.name = res.data.detail.name;
          app.User.telephone = res.data.detail.telephone;
          app.User.ic_card = res.data.detail.id_card
          that.setData({
            realname:res.data.detail.name,
            telephone1:res.data.detail.telephone,
            ic_card:res.data.detail.id_card
          })
          if (res.data.detail.is_active == true){
            app.User.is_active = "正常"
            that.setData({
              is_active:"正常",
            })
          }
          else{
            app.User.is_active = "禁用"
            that.setData({
              is_active:"禁用"
            })
          }
          if (res.data.detail.sex == "0"){
            app.User.sex = "女"
            that.setData({
              sex:"女"
            })
          }
          else{
            app.User.sex = "男"
            that.setData({
              sex:"男"
            })
          }
        }
        else{
          wx.showToast({
            title: '服务器响应失败！',
            icon: 'none',
            duration: 1000
          })
        }
      }
    })
  },
  gettelephone(e){
    this.setData({
      telephone:e.detail.value
    })
  },
  goxguser(){
    wx.navigateTo({
      url: '../xguser/xguser',
    })
  },
  godeluser(){
    var that = this
    wx.showModal({
      title: '提示',
      content: '是否确定删除',
      success (res) {
        if (res.confirm) {
          wx.request({
            url: 'https://www.skylineacg.xyz/api/su_delete/',
            method:'POST',
            data:{
              telephone:that.data.telephone1
            },
            success(res){
              app.User.name = "",
              app.User.telephone = "",
              app.User.sex = "",
              app.User.ic_card = "",
              app.User.is_active = "",
              wx.navigateTo({
                url: '../seeuser/seeuser',
              })
            }
          })
        } else if (res.cancel) {
          wx.navigateTo({
            url: '../seeuser/seeuser',
          })
        }
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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
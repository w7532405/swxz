// pages/detail/detail.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    realname:"",
    telephone:"",
    sex:"",
    ic_card:"",
    is_active:""
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    wx.request({
      url: 'https://www.skylineacg.xyz/api/detail/',
      method:'POST',
      data:{
        open_id:app.globalData.appid
      },
      success(res){
        // console.log(res.data)
        if (res.data.status == true){
          that.setData({
            realname:res.data.user.name,
            telephone:res.data.user.telephone,
            ic_card:res.data.user.id_card,
            sex:res.data.user.sex
          })
          if (res.data.user.is_active == true){
            that.setData({
              is_active:"正常"
            })
          }
          else{
            that.setData({
              is_active:"禁用"
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
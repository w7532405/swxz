// pages/tongguo/tongguo.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */

  data: {
    is_supper:false
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      is_supper:app.Is.is_supper
    })
  },
  goshowall(){
    wx.navigateTo({
      url: '../showall/showall',
    })
  },
  goxttxz(){
    wx.navigateTo({
      url: '../xttxz/xttxz',
    })
  },
  goshenhe(){
    wx.navigateTo({
      url: '../txshenhe/txshenhe',
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
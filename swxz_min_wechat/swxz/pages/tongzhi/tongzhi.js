// pages/tongzhi/tongzhi.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    xiaoxi:[],
    is_supper:false,
    is_null:true
  },
  gotianjia(){
    wx.navigateTo({
      url: '../tianjia/tianjia',
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    that.setData({
      is_supper:app.Is.is_supper
    })
    wx.request({
      url: 'https://www.skylineacg.xyz/api/wx_advise/',
      method: 'GET',
      success(res){
        // console.log(res.data.datas)
        if(res.data.status == true){
          that.setData({
            xiaoxi:res.data.datas,
          })
          if (res.data.datas.length > 0){
            that.setData({
              is_null:false
            })
          }
        }
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
    var that = this
    wx.request({
      url: 'https://www.skylineacg.xyz/api/wx_advise/',
      method: 'GET',
      success(res){
        console.log(res.data)
        if(res.data.status == true){
          that.setData({
            xiaoxi:res.data.datas
          })
        }
      }
    })
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
// pages/xttxz/xttxz.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    title:'',
    adress:'',
    name:'',
    starttime:'',
    endtime:'',
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },
  gettitle(e){
    this.setData({
      title:e.detail.value
    })
  },
  getadress(e){
    this.setData({
      adress:e.detail.value
    })
  },
  getname(e){
    this.setData({
      name:e.detail.value
    })
  },
  getstarttime(e){
    this.setData({
      starttime:e.detail.value
    })
  },
  getendtime(e){
    this.setData({
      endtime:e.detail.value
    })
  },
  sumbit_tz(){
    var that = this
    wx.request({
      url: 'https://www.skylineacg.xyz/api/wx_passper/',
      method: 'POST',
      data:{
        pass_name:that.data.title,
        pass_address:that.data.adress,
        user_name:that.data.name,
        user_starttime:that.data.starttime,
        user_stoptime:that.data.endtime,
        open_id:app.globalData.appid
      },
      success(res){
        // console.log(res.data)
        if(res.data.status == true){
          wx.switchTab({
            url: '../tongguo/tongguo',
          })
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
// pages/tianjia/tianjia.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    title:'',
    content:''
  },
  gettitle(e){
    this.setData({
      title:e.detail.value
    })
  },
  getcontent(e){
    this.setData({
      content:e.detail.value
    })
  },
  sumbit_tz(){
    var that = this
    wx.request({
      url: 'https://www.skylineacg.xyz/api/wx_advise/',
      method: 'POST',
      data:{
        nickname:app.globalData.nickname,
        title:that.data.title,
        text:that.data.content
      },
      success(res){
        // console.log(res.data)
        if (res.data.status == true){
          wx.switchTab({
            url: '../tongzhi/tongzhi',
          })
        }
        else{
          wx.showToast({ //这里提示失败原因
            title: '服务器连接错误！',
            icon: 'none',
            duration: 1500
           })
        }
      },
      fail(){
        wx.showToast({ //这里提示失败原因
          title: '服务器连接错误！',
          icon: 'none',
          duration: 1500
         })
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(app.globalData.nickname)
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
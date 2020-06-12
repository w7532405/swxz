// pages/have/have.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    number:"",
    password:""
  },
  getnumber(e){
    // console.log(e.detail.value)
    this.setData({
      number:e.detail.value
    })
  },
  getpassword(e){
    // console.log(e.detail.value)
    this.setData({
      password:e.detail.value
    })
  },
  submit(){
    var that = this
    if ((that.data.number.length)>=11){
      wx.request({
        url: 'https://www.skylineacg.xyz/api/login/',
        method:'POST',
        data:{
          telephone:that.data.number,
          password:that.data.password,
          open_id:app.globalData.appid
        },
        success(res){
          console.log(res.data)

        }
      })
    }
    else{
      wx.showToast({ //这里提示失败原因
        title: '账号长度不够',
        icon: 'none',
        duration: 1000
       })
    }
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
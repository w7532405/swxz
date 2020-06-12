// pages/shenhe/shenhe.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    infos:[],
    content1:''
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    wx.request({
      url: 'https://www.skylineacg.xyz/api/wx_dayshare/',
      method: 'GET',
      success(res){
        console.log(res.data)
        that.setData({
          infos:res.data.datas
        })
      }
    })
  },
  get_sharetext(e){
    // console.log(e.detail.value)
    this.setData({
      content1:e.detail.value
    })
  },
  submit_info(){
    var that = this
    if (that.data.content1){
      wx.request({
        url: 'https://www.skylineacg.xyz/api/wx_dayshare/',
        method: 'POST',
        data:{
          open_id:app.globalData.appid,
          nick_name:app.globalData.nickname,
          share_text:that.data.content1,
          pho_url:app.globalData.userInfo
        },
        success(res){
          console.log(res.data)
          if (res.data.status == true){
            wx.showToast({ 
              title: '发布成功!',
              icon: 'success',
              duration: 1500
             })
             wx.switchTab({
               url: '../shenhe/shenhe',
             })
          }
        }
      })
    }
    
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
      url: 'https://www.skylineacg.xyz/api/wx_dayshare/',
      method: 'GET',
      success(res){
        console.log(res.data)
        that.setData({
          infos:res.data.datas
        })
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
// pages/txshenhe/txshenhe.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    all_txz:[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    wx.request({
      url: 'https://www.skylineacg.xyz/api/wx_check_passper/',
      method: 'GET',
      success(res){
        console.log(res.data)
        if(res.data.status == true){
          that.setData({
            all_txz:res.data.datas
          })
        }
      }
    })
  },
  agree(e){
    var that = this
    // console.log(e.currentTarget.dataset.index)
    var index = e.currentTarget.dataset.index
    // console.log(that.data.all_txz[index].pass_name)
    
    wx.request({
      url: 'https://www.skylineacg.xyz/api/wx_check_passper/',
      method: 'POST',
      data:{
        open_id:app.globalData.appid,
        pass_name:that.data.all_txz[index].pass_name
      },
      success(res){
        // console.log(res.data)
        if(res.data.status == true){
         wx.redirectTo({
           url: '../txshenhe/txshenhe',
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
    var that = this
    wx.request({
      url: 'https://www.skylineacg.xyz/api/wx_check_passper/',
      method: 'GET',
      success(res){
        console.log(res.data)
        // if(res.data.status == true){
        //   that.setData({
        //     xiaoxi:res.data.datas
        //   })
        // }
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
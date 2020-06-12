// pages/xguser/xguser.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    show_realname:"111",
    show_telephone:"456",
    show_ic_card:"4654",
    show_sex:"男",
    show_is_active:"正常",
    realname:"",
    telephone:"",
    ic_card:"",
    sex:"",
    is_active:"",
    sex_value:"",
    is_active_value:"",
    array:["女", "男"],
    array1:["禁用", "正常"],
    is_select:false,
    is_select1:false
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
  bindPickerChange1(e){
    // console.log(e.detail.value)
    this.setData({
      is_active:e.detail.value
    })
    if(e.detail.value == 0){
      this.setData({
        is_active_value:"禁用",
        is_select1:true
      })
    }
    else{
      this.setData({
        is_active_value:"正常",
        is_select1:true
      })
    }
  },
  getname(e){
    this.setData({
      realname:e.detail.value
    })
  },
  gettelephone(e){
    this.setData({
      telephone:e.detail.value
    })
  },
  getidcard(e){
    console.log(this.data.ic_card)
    this.setData({
      ic_card:e.detail.value
    })
  },
  submit1(){
    wx.navigateTo({
      url: '../supperson/supperson',
    })
  },
  submit(){
    var that = this
    wx.request({
      url: 'https://www.skylineacg.xyz/api/su_change/',
      method: 'POST',
      data:{
        telephone:app.User.telephone,
        name:that.data.realname,
        telephone1:that.data.telephone,
        id_card:that.data.ic_card,
        sex:that.data.sex,
        is_active:that.data.is_active
      },
      success(res){
        wx.navigateTo({
          url: '../supperson/supperson',
        })
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
    this.setData({
      show_realname:app.User.name,
      show_sex:app.User.sex,
      show_telephone:app.User.telephone,
      show_ic_card:app.User.ic_card,
      show_is_active:app.User.is_active
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
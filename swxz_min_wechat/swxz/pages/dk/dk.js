// pages/dk/dk.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    is_dj:true,
    region:[],
    array:["否", "是"],
    is_select:false,
    is_select1:false,
    is_select2:false,
    is_dk:false,
    dk_nr:"",
    yq_value:"",
    yq:"",
    fr_value:"",
    fr:"",
    ks_value:"",
    ks:"",
    show_adress:"",
    qt_bl:"",
    telephone:""
  },
  change(e){
  // console.log(e.detail.value)
    this.setData({
      region:e.detail.value,
      is_dj:false
    })
    // console.log(this.data.region[0])
  },
  getadress(e){
    // console.log(e.detail.value)
    this.setData({
      dk_nr:e.detail.value
    })
  },
  getqtbl(e){
    this.setData({
      qt_bl:e.detail.value
    })
  },
  bindPickerChange1(e){
    // console.log(e)
    this.setData({
      fr:e.detail.value
    })
    if (e.detail.value == 0){
      this.setData({
        fr_value:"否",
        is_select:true
      })
    }
    else{
      this.setData({
        fr_value:"是",
        is_select:true
      })
    }
  },
  bindPickerChange2(e){
    // console.log(e)
    this.setData({
      yq:e.detail.value
    })
    if (e.detail.value == 0){
      this.setData({
        yq_value:"否",
        is_select1:true
      })
    }
    else{
      this.setData({
        yq_value:"是",
        is_select1:true
      })
    }
  },
  bindPickerChange3(e){
    // console.log(e)
    this.setData({
      ks:e.detail.value
    })
    if (e.detail.value == 0){
      this.setData({
        ks_value:"否",
        is_select2:true
      })
    }
    else{
      this.setData({
        ks_value:"是",
        is_select2:true
      })
    }
  },
  submit(){
    var that = this
    wx.request({
      url: 'https://www.skylineacg.xyz/api/wx_daytext/',
      method:'POST',
      data:{
        province:that.data.region[0],
        city:that.data.region[1],
        area:that.data.region[2],
        de_addr:that.data.dk_nr,
        hot:that.data.fr,
        danger_area:that.data.yq,
        cough:that.data.ks,
        other_cases:that.data.qt_bl,
        telephone:that.data.telephone
      },
      success(res){
        if (res.data.status == true){
          if(res.data.result == "1"){
            wx.showToast({
              title: '提交成功！',
              icon:'success',
              duration:1000
            })
            wx.switchTab({
              url: '../index/index',
            })
          }
        }
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    // console.log(app.Is.regist)
    if (app.Is.regist == true){
      wx.request({
        url: 'https://www.skylineacg.xyz/api/wx_is_day/',
        method:'POST',
        data:{
          open_id:app.globalData.appid
        },
        success(res){
          console.log(res.data)
          if (res.data.is_day == "1"){
            wx.switchTab({
              url: '../index/index',
            })
            wx.showToast({
              title: '一天只能打卡一次',
              icon: 'none',
              duration:2000
            })
          }
          if (res.data.status == true){
            that.setData({
              telephone:res.data.telephone,
            })
          }
          else{
            wx.showToast({
              title: '服务器响应失败！',
              icon:'none',
              duration:1000
            })
          }
        }
      })
    }
    else{ 
    wx.switchTab({
      url: '../index/index'
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
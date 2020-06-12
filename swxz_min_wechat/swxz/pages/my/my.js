// pages/my/my.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {  
    avatarUrl:"../../icons/weixin.png",
    nickName:"",
    id:"",
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    is_bind:false,
    realName:"",
    is_supperson:false
  },
  bindGetUserInfo(e){
    // console.log(this.data.canIUse)
    // console.log(e.detail.userInfo)
    app.globalData.userInfo=e.detail.userInfo.avatarUrl
    app.globalData.nickname=e.detail.userInfo.nickName
    var that=this
    that.setData({
      avatarUrl:e.detail.userInfo.avatarUrl,
      nickName:e.detail.userInfo.nickName,
      canIUse:!that.data.canIUse
    }),
    wx.login({
      success:function(res){
        wx.request({
            //获取openid接口
          url: 'https://www.skylineacg.xyz/api/wx_return/',
          data:{
            appid:"wxa003021347820d87",
            secret:"b1fef09af2669506aa47bcd1e0f2ab28",
            js_code:res.code,
            grant_type:'authorization_code'
          },
          method:'GET',
          success:function(res){
            console.log(res)
            that.setData({
              id:res.data.openid
            })
            app.globalData.appid = that.data.id
            wx.request({
              url: 'https://www.skylineacg.xyz/api/getwxid/',
              method:'POST',
              data: {
                pho_url:that.data.avatarUrl,
                wx_openid: that.data.id
              },
              success(res){
                console.log(res)
                if (res.data.status == true) {
                  app.Is.regist = res.data.regist
                  app.Is.is_supper = res.data.is_super
                  app.User.name = res.data.realName
                  console.log(app.Is.regist)
                  if(res.data.is_super == true){
                    that.setData({  
                      is_supperson:true
                    })
                  }
                  that.setData({
                    is_bind:res.data.regist,
                    realName:res.data.realName
                  })
                  if(res.data.regist == false){
                    wx.showModal({
                      title: '温馨提示',
                      content: '您还没有注册/绑定,是否前往相关界面',
                      success (res) {
                        if (res.confirm) {
                          wx.navigateTo({
                            url: '../ishave/ishave',
                          })
                        }
                        else if (res.cancel) {
                          wx.switchTab({
                            url: '../my/my',
                          })
                        }
                      }
                    })
                  } 
                  
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
                  duration: 1000
                 })
              }
            })
          }
        })
      }
    })
    
  },
  godetail(){
    var that = this
    if (that.data.is_bind){
      wx.navigateTo({
        url: '../detail/detail',
      })
    }
    else{
      wx.navigateTo({
        url: '../ishave/ishave',
      })
    }
  },
  gosupperson(){
    wx.navigateTo({
      url: '../supperson/supperson',
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    wx.request({
      url: 'https://www.skylineacg.xyz/api/getwxid/',
      method:'POST',
      data: {
        pho_url:app.globalData.userInfo,
        wx_openid: app.globalData.appid
      },
      success(res){
        console.log(res)
        if (res.data.status == true) {
          app.Is.regist = res.data.regist
          app.Is.is_supper = res.data.is_super
          app.User.name = res.data.realName
          console.log(app.Is.regist)
          if(res.data.is_super == true){
            that.setData({  
              is_supperson:true
            })
          }
          that.setData({
            is_bind:res.data.regist,
            realName:res.data.realName
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
  handleContact (e) {
    console.log(e.detail.path)
    console.log(e.detail.query)
},
  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    var that = this
    wx.request({
      url: 'https://www.skylineacg.xyz/api/getwxid/',
      method:'POST',
      data: {
        pho_url:app.globalData.userInfo,
        wx_openid: app.globalData.appid
      },
      success(res){
        console.log(res)
        if (res.data.status == true) {
          app.Is.regist = res.data.regist
          app.Is.is_supper = res.data.is_super
          app.User.name = res.data.realName
          console.log(app.Is.regist)
          if(res.data.is_super == true){
            that.setData({  
              is_supperson:true
            })
          }
          that.setData({
            is_bind:res.data.regist,
            realName:res.data.realName
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
          duration: 1000
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